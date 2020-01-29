# Loops - while, for, break, continue

test1 = 7
test2 = "7"
if (test1 == test2):
    print("yup")
else:
    print("nope")           # this one prints. hm, "7" != 7


# WHILE LOOP
names = []                  # empty list array thing
while (len(names) < 5):     # iteration 0, 1, 2, 3, 4, goes to 5, fails
    person = input("Enter a name: ")
    names.append(person)
print(names)


# WHILE LOOP - GUESSING GAME USING 'BREAK'
while (True):               # just keep going forever and ever
    guess = int(input("Enter your guess from 0-10: "))
    if (guess == 7):
        print("You got it right!")
        break


# Let's make the game above cooler by making it a random number each time. So, let's import the 'random' module.
# test = random.randint(0, 10)      # DOES NOT WORK! Cannot use anything from a module if it's called BEFORE its import!s

import random
unknown = random.randint(0, 10)     # random number from 0 to 10 inclusive
while (True):
    guess = int(input("Enter your guess: "))
    if (guess == unknown):
        print("You got it right!")
        break


# FOR LOOPS
games = ["Fire Emblem: Three Houses", "Pokemon Sword", "Octopath Traveler", "Golden Sun Trilogy Remastered"] # print all titles
for titles in games:    # that's literally it. for loops are an iterator, we just declare a variable and print lol
    print(titles)       # so much easier than Java. ugh i miss my int i = 0; i < array.length; i++


fruits = ["apples", "pears", "", "oranges", "", "", "bananas"]  # some left blank - don't print these! use "continue".
for beep in fruits:
    if beep == "":
        continue        # SKIP THIS ITERATION! GO TO THE NEXT ONE!
    else:
        print(beep)


string = "This is my string."
for char in string:
    print(char)         # print all letters in string lol


for x in range(0, 10):
    print(x)            # ranges! 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.


# Given a dictionary with lists, print all elements
family = { "Matthew" : ["Mark", "Luke", "John"], "Mary" : ["James", "Bob", "Greg"], "Joseph" : ["AAA", "BBB", "CCC"]}

for parent in family:
    print("Parent name:", parent)
    for child in family[parent]:
        print("Child name:", child)