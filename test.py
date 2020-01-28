# Statements

print("Hello, World!")
print("The average of 4 and 8 is: ", (4 + 8) / 2)

# Variables

age = 20
print("My age is", age) # comma adds a space

number1 = 10
number2 = 20
print("The average is", (number1 + number2) / 2)

# Prompt user for input: the input() function

number3 = input("Enter first number: ")
number4 = input("Enter second number: ")
print(number3)
print(number4)
print(type(number3))
print(type(number4))
# print("Average is", (number3 + number4) / 2) - fails because it is of type String. can use type() to find out

# Redoing it - casting Strings to float values
number5 = input("Enter first number: ")
number6 = input("Enter second number: ")
print("Average of these two numbers:", (float(number5) + float(number6)) / 2 ) # conversion can also be done when assigning, float(input())

# Strings

String = "String"
print(String[0])    # S, 0-based
print(len(String))  # 6

# String indexes and slicing - [x:y]

print(String[0:3])  # slicing - gives Str
print(String[-1])   # negative indexes start counting backwards - g
print(String[-2])   # n
print(String[2:])   # grabbing from 2nd index, to the rest of the string (leave 2nd param empty)
print(String[:4])   # grabbing from beginning, up until 4th index