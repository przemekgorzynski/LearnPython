# Script moves mouse X times every 30 sec.

import sys
import subprocess
import pkg_resources


# Check if mouse library in installed and install if not
required = {'mouse'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)


import time, datetime, mouse

help_message = """

Script moves mouse coursor X times in a loop every 60 sec. X is provided as argument
example:
mouse_move.py 40

"""

# check if atguments were passed to script
try:                                                                
    sys.argv[1]
except IndexError:
    print("No args given. Run mouse_move.py --help for help")
    quit()

# check first argument
if sys.argv[1] == "--help" or sys.argv[1] == "-h":                  
    print(help_message)
    quit()

# check current date
now=datetime.datetime.now()
print('')
print("Start time:", now.strftime("%H:%M:%S"))

print("Your idle time is:", int(sys.argv[1]), "minutes")

i=0

while i < int(sys.argv[1]):
   print("Minutes passed:", i, " | ", "Minutes left:", int(sys.argv[1])-i)
   mouse.move(1, 1, absolute=False, duration=0.2)
   time.sleep(60)
   i += 1