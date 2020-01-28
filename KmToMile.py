# Make a program that accepts a user input in kilometres and output that number in miles
# 1 mile = 1.609344 kilometres

km = float(input("Enter number of kilometres: "))

miles = km / 1.609044

print("That is equivalent to", round(miles, 2), "miles.") # round(arg, num) rounds arg to num of decimal places