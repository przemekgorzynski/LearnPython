# Write a Python program which accepts the radius of a circle from the user and compute the area
from math import pi

r = float(input("Please provide radius value: \n"))
print("Circle area with radius "  + str(r) + " is: " + str(pi * r**2))