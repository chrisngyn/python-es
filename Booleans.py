# Create a program and store your age. Ask the user for input and print if it is greater than, equal to, or less than your age
# test1 = 10.5
# test2 = int(test1)
# print(test2) - 10

my_age = 20
user_age = int(input("Enter your age: "))

if (my_age < user_age):
    print("User is older than I am")
elif (my_age == user_age):
    print("We are the same age")
else:
    print("I am older than you")