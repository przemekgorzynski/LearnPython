# Script that makes dump of postgresql database, create it and remove ones older than two days
# Creates file .pgpass in user's home directory with content *:*:database:username:password  and chmod 0600
# Update : BASE64PASSWORD, *:*:database:username

import os

prepare_pass = """ echo "BASE64PASSWORD=" > password """                                    # Write database base64 decoded password to file
os.system("bash -c '%s'" % prepare_pass)

pgpass_script = """ echo "*:*:database:username:"`base64 -d password`"" > ~/.pgpass """           # prepare file with pgpasswords
os.system("bash -c '%s'" % pgpass_script)

os.chmod("/root/.pgpass", 0o600)

env_script = """ export PGPASSFILE='~/.pgpass' """                                      # Export variable
os.system("bash -c '%s'" % env_script)

pg_dump_script = """ pg_dump -h localhost -U awx --no-password awx | gzip > backup-"`date '+%Y-%m-%d-%H:%M'`".gz """    # make backup
os.system("bash -c '%s'" % pg_dump_script)

print ( "files to remove\n"  )

list_script = """ if [[ $? == "0" ]]; then find . -mtime +2 -iname "backup*.gz" -exec /usr/bin/ls {} \;; fi  """        # list files older than 2 days
os.system("bash -c '%s'" % list_script)

old_remove_script = """ if [[ $? == "0" ]]; then find . -mtime +2 -iname "backup*.gz" -exec /usr/bin/rm {} \;; fi  """  # remove files older than 2 dys
os.system("bash -c '%s'" % old_remove_script)

os.remove("password")                           # cleab temporary files
os.remove("/root/.pgpass")
