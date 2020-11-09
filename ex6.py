# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

numbers = list(map(str, input( " Please provide numbers separated by comma: ").split(",")))

print ("List: " + str(numbers))

x = tuple(numbers) 
print ("Tuple: " + str(x))