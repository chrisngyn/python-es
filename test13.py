# File handling basics - creating, reading, writing. open(file_name, mode)

file1 = open("my_file1.txt", "r")           # open my_file.txt in read mode
print(file1.read())

print("")

file2 = open("my_file2.txt", "w")           # this will write on the file - be careful as it will OVERWRITE the current content that are on it
file2.write("This text will overwrite anything currently in this file!!")
file2 = open("my_file2.txt", "r")
print(file2.read())

print("")

file3 = open("my_file3.txt", "a")           # append mode - doesn't overwrite, appends text to this file
file3.write("\nThis text is being added after through a Python program!!")
file3 = open("my_file3.txt", "r")
print(file3.read())

# the write and append modes can create a file, if we pass a file name that doesn't exist, one will be created
# though, the read mode will return an error trying to read a file that doesn't exist

# file4 = open("my_file4.txt", "x")           # x mode is used to create a file, running this a second time though will return an error since it exists

# open("/Users/user/Desktop/new_file.txt", "x")   # you can create files in a new directory, just print the full path