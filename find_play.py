#!/usr/bin/env python3
# Find and play random movie from NAS backup directory.
import os
import sys
import random
import subprocess

def mount(path):
    command = 'sudo mount -t cifs -o credentials=/.smbcredentials,nounix,uid=1000,gid=100,dir_mode=0770,file_mode=0660 //192.168.0.61/other /home_nas_backup'
    if os.path.exists(path):
        None
    else:
        try:
            subprocess.run([command], shell=True)
        except Exception:
            pass

def list_files(path):
    os.chdir(path)
    for root, dirs, files in os.walk(path):
    	for file in files:
    		file_list.append(os.path.join(root,file))
                
def get_random(file_list):
    return random.choice(file_list)

def play_movie(movie):
     command= "/usr/bin/vlc {} 2>/dev/null".format(movie)
     subprocess.run([command], shell=True)

file_list = []

try:  # check if atguments were passed to script
    path = sys.argv[1]
except:
    path = '/home_nas_backup/new'

print(path)
mount(path)
list_files(path)
movie=get_random(file_list)
print(movie)
play_movie(movie)
