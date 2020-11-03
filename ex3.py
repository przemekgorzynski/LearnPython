# Write a Python program to display the current date and time.
import datetime

print("Current data and time")
now=datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))