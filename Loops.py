import random

# Ask the user for eight names and store in a list. Pick a random one and print it.

names = []                  # len 0
while (len(names) < 8):     # or for x in range(0, 8) - 0 1 2 3 4 5 6 7
    name = input("Enter a name: ")
    names.append(name)      # len is now 8 at the end of it

rand = random.randint(0, 7) # random number 0, 1, 2, 3, 4, 5, 6, 7 - list is 0 based
print(names[rand])


# Create a guessing game with names of colours. Randomly choose a new one at the beginning of the game.
# At the end of each game, ask the user if they want to play again.

colours = ["red", "blue", "green"]  # length 3, indexes 0 1 2

while (True):
    the_chosen_one = colours[ random.randint(0, len(colours)-1) ]
    user_guess = input("Guess a colour: ").lower()

    while (True):
        if (the_chosen_one == user_guess):
            print("You got it right!")
            break                   # ONLY OUT OF THIS LOOP. NOT BOTH! IT'S GOING TO CONTINUE LOOP 1
        else:
            user_guess = input("Nope, try again: ")
    
    print ('You guessed it, I was thinking of ' + the_chosen_one + '.')
    cont = input("Do you want to play again? Type 'no' to quit. ")

    if (cont == "no"):
        break

print("Bye!")