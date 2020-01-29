# Dictionaries. The best data structure in the world

JohnGreen = { "FNAME" : "John", "LNAME" : "Green", "BIRTHYEAR" : 1980 }
print(type(JohnGreen))
print(JohnGreen)
print(JohnGreen["FNAME"])       # accessing specific keys in dictionary
print("\n")

JohnGreen["BIRTHYEAR"] = 1979   # reassigning a value to a key
JohnGreen["AGE"] = 41           # adding new key and value to dictionary
print(JohnGreen)
print("\n")

JohnGreen["CHILDREN"] = ["Matthew", "Mark"]     # you can add a list as a key! JohnGreen["CHILDREN"] now returns list data type
print(type(JohnGreen["CHILDREN"]))              # returns list - so we can even APPEND onto this
print(JohnGreen)
JohnGreen["CHILDREN"].append("Luke")
JohnGreen["CHILDREN"].append("John")
print(JohnGreen)
print("\n")

# print(JohnGreen["NOPE"]) if we try to get the value of a key that doesn't exist we get an error, so instead try ".get(key)"
print(JohnGreen["FNAME"])
print(JohnGreen.get("FNAME"))
print(JohnGreen.get("creditcardnumbers", "DOESN'T EXIST"))  # will return that message if no match lol, "None" by default
print("\n")

# Alt way of accessing keys
first_name = "FNAME"
print(JohnGreen[first_name])
print(JohnGreen)
JohnGreen.clear()   # Clear dictionary!
print(JohnGreen)