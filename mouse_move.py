# Script moves mouse X times every 30 sec.

import sys, time, datetime

help_message = """
*** TO USE THIS SCRIPT INSTALL MOUSE LIBRARY: *** \nsudo apt install python-pip3\npip3 install mouse

Script moves mouse coursor X times in a loop every 60 sec. X is provided as argument
example:
mouse_move.py 40

"""

try:                                                                # check if atguments were passed to script
    sys.argv[1]
except IndexError:
    print("No args given. Run mouse_move.py --help for help")
    quit()

if sys.argv[1] == "--help" or sys.argv[1] == "-h":                  
    print(help_message)
    quit()

import mouse

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