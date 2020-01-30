# Validating inputs. Grade is 0-10 but accepts any #. Absences can be greater than total. Total # of class can be negative.
# Not only do we need to validation the data CONTENTS, but also the data TYPE. cause someone can enter a STRING!!

data_validation = False

while (data_validation == False):
    grade1 = float(input("Enter first grade: "))

    if (grade1 < 0 or grade1 > 10):
        print("Value not allowed!")
    else:
        data_validation = True
        continue

data_validation = False

while (data_validation == False):
    grade2 = float(input("Enter second grade: "))

    if (grade2 < 0 or grade2 > 10):
        print("Value not allowed!")
    else:
        data_validation = True
        continue

total_classes = int(input("Enter total number of classes: "))       # should also do data validation for these but
absences = int(input("Enter number of missed classes: "))           # i don't really care lol

average_grade = (grade1 + grade2) / 2
attendance = ((total_classes - absences) / total_classes) * 100

print("Average grade: ", average_grade)
print("Attendance rate: ", attendance)
if (average_grade >= 6 and attendance >= 80):
    print("You passed!")
elif (average_grade >= 6 and attendance < 80):
    print("You failed - reason: attendance too low.")
elif (average_grade < 6 and attendance >= 80):
    print("You failed - reason: grades too low.")
else:
    print("You failed - reason: grades too low and attendance too low.")


# TRY AND EXCEPT STATEMENTS - THINK TRY AND CATCH IN JAVA
try:
    number = float(input("Enter a number: "))
    print(f"The number you entered was {number}.")  # alternative way of printing - STRING INTERPOLATION!
except:
    print('Hey! Bad input!')                        # execute if the above is going to throw some kind of error