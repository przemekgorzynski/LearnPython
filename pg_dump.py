# make backup og postgresql database
import datetime, sys, os

help_message = """
Script that makes dump of postgresql AWX database, create it and remove ones older than two days
Run script:  backup.py BASE64_ENCODED_PG_PASSWORD  PATH_TO_BACKUPS
example:
backup.py  cGFzc3dvcmQ=  /var/pg_backup
"""

try:                                                                # check if atguments were passed to script
    sys.argv[1]
except IndexError:
    print("No args given. Run backup.py --help for help")
    quit()

if sys.argv[1] == "--help" or sys.argv[1] == "-h":                  # if firs targument is -h or --help display help message
    print(help_message)
    quit()

pg_password = sys.argv[1]                                           # write provided parameters to variables
log_path = sys.argv[2]

if not os.path.exists(log_path):                                    # cechk if backup dir exists and if not create
    os.makedirs(log_path)

#print(pg_password)
#print(log_path)

f = open( 'password', 'w' )                                                             # write pg_password to file
f.write(pg_password)
f.close()

home=os.environ['HOME']                                                 # set path to pgpass file to variable
full_path=home + "/.pgpass"

pgpass_script = """ echo "*:*:awx:awx:"`base64 -d password`"" > ~/.pgpass """           # prepare pgpass file with base64 decoded pg_dump password
os.system("bash -c '%s'" % pgpass_script)

os.chmod(full_path, 0o600)                                                        # Manage pgpass file

os.environ['"PGPASSFILE"'] = "~/.pgpass"                                                # Export needed variables
os.environ['log_path'] = log_path

#print(os.environ['"PGPASSFILE"'])
#print(os.environ['log_path'])

pg_dump_script = """ pg_dump -h localhost -U awx --no-password awx | gzip > $log_path/backup-"`date '+%Y-%m-%d-%H:%M'`".gz """          # make backup
os.system("bash -c '%s'" % pg_dump_script)

#print ( "files to remove\n"  )

list_script = """ if [[ $? == "0" ]]; then find $log_path -mtime +2 -iname "backup*.gz" -exec /usr/bin/ls {} \;; fi  """        # list files to delete -  older than 2 days
os.system("bash -c '%s'" % list_script)

old_remove_script = """ if [[ $? == "0" ]]; then find $log_path -mtime +2 -iname "backup*.gz" -exec /usr/bin/rm {} \;; fi  """  # remove files older than 2 dys
os.system("bash -c '%s'" % old_remove_script)

os.remove("password")                           # clean temporary files
os.remove(full_path)
