# Lists: because Python doesn't have a native array data structurex
stringNames = "Matthew, Mark, Luke, John"   # what's the first name? how to add another name? how many names do we have?
listNames = ["Matthew", "Mark", "Luke", "John"]
print(type(stringNames))
print(type(listNames))

print(len(listNames))   # number of names
print(listNames[0])     # first name
print(listNames[-1])    # last name
print(listNames[:2])    # all up to index 2, meaning index [0] and [1]
print(listNames)
listNames[0] = "Jesus"
listNames.append("Zuckerberg")  # damn python is way cooler than java
listNames.insert(1, "James")    # at index 1, put James, put everything over
print(listNames)
print("\n")

# More list stuff:
print(listNames)
print(listNames.pop())  # removes last element and returns it
print(listNames.pop(2)) # index 2
listNames.remove("James")       # you can search and remove by specific elements
print(listNames)
print("\n")


# Tuples: lists, but immutable; never changing
months = ("January", "February", "March", "April", "May")
print(months)
print(type(months))
print("\n")
# months[0] = "December" - not allowed


# Merging - you can merge two lists or two tuples, but not a list and a tuple
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 0]
list3 = list1 + list2
print(list3)