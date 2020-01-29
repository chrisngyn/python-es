# Boolean and some control flow (if, elif, else)

myBoolean1 = True   # no quotation marks, capital T or F
myBoolean2 = False

num1 = 1000
num2 = 1100

print(num1 < num2)  # wow I love python
print(num1 == num2)

num3 = float(input("Enter number 1: "))
num4 = float(input("Enter number 2: "))

if (num3 > num4):   # I miss you, curly braces :(
    print(num3, "is greater than", num4)
elif (num3 == num4):
    print("BOTH NUMBERS ARE EQUAL")
else:
    print(num3, "is less than", num4)