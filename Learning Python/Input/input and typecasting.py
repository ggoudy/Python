# Input can be asked of the user by using input()
input()

# The line above does not store the value
# To store the input, assign a variable like so 
input1 = input()
print(input1)

# Input can contain a message to tell the user what to input
input2 = input("Please enter a number: ")
print(input2)

# The input given becomes a string by default
# Using typecasting, we can indicate to store 
# the value as an integer, float or string

input3 = int(input("Please enter another number to be stored as an integer: "))
print(input3, "is a", type(input3))

input4 = float(input("Please enter another number to be stored as a float: "))
print(input4, "is a", type(input4))

input5 = str(input("Please enter a value to be stored as a string: "))
print(input5, "is a", type(input5))
