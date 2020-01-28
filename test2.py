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


# Tuples: lists, but immutable; never changing
months = ("January", "February", "March", "April", "May")
print(type(months))
# months[0] = "December" - not allowed