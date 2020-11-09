# Write a Python program to accept a filename from the user and print the extension of that.

import os

filename = input("Please provide filename with extension: ")
print ("File: " + filename)
print("Extension of file: " + os.path.splitext(filename)[1].strip('.'))