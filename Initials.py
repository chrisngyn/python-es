# Create a program that asks for a users first, middle, and last name, and print their initials (3 different inputs)

first = input("Enter first name: ")
middle = input("Enter your middle name: ")
last = input("Enter your last name: ")

initials = first[:1] + middle[:1] + last[:1] # or you can just do [0] lol
print(initials)


# Create a program that takes this number: 123-12345-67890 and splits it into 3 lines, 123, 12345, 56789

input = "123-12345-67890"
print("Code 1:", input[0:3])    # 0 to 3, means 0, 1, 2. NOT including 3
print("Code 2:", input[4:9])    # String[inclusive:exclusive]
print("Code 3:", input[10:])