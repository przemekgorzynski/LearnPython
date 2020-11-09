# Write a Python program to display the first and last colors from the given list. 

colours = list(map(str, input( "Please provide colours separated by comma: ").split(",")))

print ("First colour: " + colours[0])
print ("Last colour: " + colours[-1])