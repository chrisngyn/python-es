# Create a program that asks a user for their birthday in DD-MM-YYYY and print out "You were born in #{MONTH}"

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

birthday = input("Type your birthday in the format DD-MM-YYYY: ")
month = int(birthday[3:5])

print("You were borth in:", months[month-1])

# Create a list with predefined names. Ask user for their name and add it to the list

names = ["Matthew", "Mark", "Luke", "John"]
nameToAdd = input("What's your name? ")
names.append(nameToAdd)
print(names)