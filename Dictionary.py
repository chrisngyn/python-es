# Create a program with a predeined dictionary for a person, include their name, gender, age, address, and phone number
# Ask user for what they want to know about the user, and print it corresponding
# [] list () tuple {} dictionary
# REMEMBER PYTHON IS CASE SENSITIVE

Chris = { "NAME" : "Christopher", "GENDER" : "M", "AGE" : 20, "ADDRESS" : "123 Intern St.", "PHONE" : "123-456-7890" }

user_query = input("What do you want to know? ").upper() # turns user input to ALL CAPS so 'name' can work, .lower() is also a thing

print(Chris.get(user_query, "DOES NOT EXIST"))  # .get(key, optional message), print(Chris[user_query]) also works