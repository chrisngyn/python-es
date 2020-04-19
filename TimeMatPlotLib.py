# Time and Pyplot exercise: create a program to help the user type faster.
# Give them a word and ask them to write it five times. Check how many seconds it took him
# to type the word at each round. In the end, tell the user how many mistakes were made and
# show a chart with the typing speed evolution during the five rounds.

# Python typing speed tester.

# 1. import the modules we need.
import matplotlib.pyplot as plt
import time

# 2. store times as a list and numbre of mistakes
times = []
mistakes = 0

# 3. begin program

print("Type the word 'programming' as fast as you can five times.")
input("Press enter to continue.") # don't want to store it. just have the user have to press enter to start.

while (len(times) < 5): # at the moment, length is 0
    start = time.time() # number of times since the epic lol
    word = input("Type 'programming': ")
    end = time.time()
    time_elapsed = end - start
    times.append(time_elapsed)

    if (word.lower() != "programming"):
        mistakes += 1

print("You made " + str(mistakes) + " mistake(s).")
print("Chart of your results:")
time.sleep(2)

x_vals = [1, 2, 3, 4, 5]
y_vals = times
plt.plot(x_vals, y_vals)
x_labels = ["1", "2", "3", "4", "5"]
plt.xticks(x_vals, x_labels)
plt.title("Your typing evolution")
plt.xlabel("Attempt")
plt.ylabel("Time in seconds")
plt.show()
