#!/usr/bin/env python3
# Find and play random movie from NAS backup directory.
import os
import sys
import random
import subprocess
import time

HELP_MESSAGE = """
Script usage:
find_play.py PATH number_of_choices
PATH - provide PATH to play file from, mandatory,  if provided 'default' = /home_nas_backup/new
number_of_choices - how many titles you will choose file from, optional, default = 7
"""

# Mount PATH if not reacheble
def mount(PATH):
    command = 'sudo mount -t cifs -o credentials=/.smbcredentials,nounix,uid=1000,gid=100,dir_mode=0770,file_mode=0660 //192.168.0.61/other /home_nas_backup'
    if os.path.exists(PATH):
        pass
    else:
        try:
            subprocess.run([command], shell=True, check=False)
            time.sleep(5)
        except Exception:
            pass

# Make list FULL_FILE_LIST with all files within PATH
def list_files(PATH):
    os.chdir(PATH)
    for root, dirs, files in os.walk(PATH):
        for file in files:
            FULL_FILE_LIST.append(os.path.join(root,file))

# Make list CHOICE_LIST of size CHOICE_LIST_SIZE with random choices from FULL_FILE_LIST                
def get_random(FULL_FILE_LIST, CHOICE_LIST_SIZE):
    for i in range(CHOICE_LIST_SIZE):
        i = random.choice(FULL_FILE_LIST)
        CHOICE_LIST.append(i)
    return CHOICE_LIST

# Print CHOICE_LIST, wait for user's choice and play choosen file
def play_movie(CHOICE_LIST):
    print('Choose movie:')
    for index, i in enumerate(CHOICE_LIST, start=1):
        print(f"{index}: {i.rsplit('/')[-1]}")
    print("And the winner is ....")
    choice = input()
    if int(choice) > len(CHOICE_LIST):
        print ("NUmber out of list range")
        quit()
    else:
        print(CHOICE_LIST[int(choice)-1])
    command= f"/usr/bin/vlc {CHOICE_LIST[int(choice)-1]} 2>/dev/null"
    subprocess.run([command], shell=True, check=False)

os.system("clear")
FULL_FILE_LIST = []
CHOICE_LIST = []

# Check arguments
try:
    sys.argv[1]
except IndexError:
    print("Uncorrect args given. Run find_play.py --help for help")
    quit()

if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print(HELP_MESSAGE)
    quit()
elif sys.argv[1] == "default":
    PATH = '/home_nas_backup/new'
else:
    PATH = sys.argv[1]

# If 2nd parameter is provided, otherwise set default value
if sys.argv[2:]:
    CHOICE_LIST_SIZE = int(sys.argv[2])
else:
    CHOICE_LIST_SIZE = 7

mount(PATH)
list_files(PATH)
CHOICE_LIST=get_random(FULL_FILE_LIST, CHOICE_LIST_SIZE)
play_movie(CHOICE_LIST)
