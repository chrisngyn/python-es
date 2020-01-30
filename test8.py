# Functions - say we use same lines of code multiple times, no need to keep typing it over and over and over
# Creating a function: "def #{FUNCTION_NAME}():" then all indented lines belong to that function

def hello(name = "there"):              # OPTIONAL ARGUMENT. IF YOU DIDN'T PUT '= ...' THEN IT MEANS IT'S MANDATORY!
    print("Hello " + name + "!")

hello()                                 # invoking
hello("Chris")


def fahr2celsius(fahr):
    celsius = (5 * (fahr - 32)) / 9     # could've just done return (5 * (fahr - 32)) / 9 but who cares
    return celsius                      # here's the difference now: you have a value that you can manipulate rather than print


print(fahr2celsius(76))
print(round(fahr2celsius(76), 2))
print("Fahr 24 to celsius is: ", fahr2celsius(76))