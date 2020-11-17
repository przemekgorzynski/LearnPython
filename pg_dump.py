# creating backup of postgresql databse using pg_dump and remove backups older than two days  ( intentionally running from crontab )
# Run script:  backup.py BASE64_ENCODED_PG_PASSWORD  PATH_TO_BACKUPS  eg.  backup.py  cGFzc3dvcmQ=  /var/pg_backup
# TODO: write execution of "-h" parameter to show help

import os, sys

pg_password = sys.argv[1]
log_path = sys.argv[2]

if not os.path.exists(log_path):
    os.makedirs(log_path)

#print(pg_password)
#print(log_path)

f = open( 'password', 'w' )                                                             # write base64 encoded pg_password to file
f.write(pg_password)
f.close()

pgpass_script = """ echo "*:*:awx:awx:"`base64 -d password`"" > ~/.pgpass """           # prepare pgpass file with base64 decoded pg_dump password
os.system("bash -c '%s'" % pgpass_script)

os.chmod("/root/.pgpass", 0o600)                                                        # Manage pgpass file

os.environ['"PGPASSFILE"'] = "~/.pgpass"                                                # Export needed variables
os.environ['log_path'] = log_path

pg_dump_script = """ pg_dump -h localhost -U awx awx | gzip > $log_path/backup-"`date '+%Y-%m-%d-%H:%M'`".gz """          # make backup
os.system("bash -c '%s'" % pg_dump_script)

#print ( "files to remove\n"  )

list_script = """ if [[ $? == "0" ]]; then find $log_path -mtime +2 -iname "backup*.gz" -exec /usr/bin/ls {} \;; fi  """        # list files to delete -  older than 2 days
os.system("bash -c '%s'" % list_script)

old_remove_script = """ if [[ $? == "0" ]]; then find $log_path -mtime +2 -iname "backup*.gz" -exec /usr/bin/rm {} \;; fi  """  # remove files older than 2 dys
os.system("bash -c '%s'" % old_remove_script)

os.remove("password")                           # clean temporary files
os.remove("/root/.pgpass")
