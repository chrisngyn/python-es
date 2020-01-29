# Control flow and loops

if (1 < 2 and 2 < 1):       # and, or, not
    print("beep")
else:
    print("boop")

if (1 < 2):
    print("i got here (1)")
elif (2 < 3):
    print("i got here (2)") # ain't gonna print.

if (3 < 4):
    print("i got here (3)")
if (4 < 5):
    print("i got here (4)")

grade1 = float(input("Enter first grade: "))
grade2 = float(input("Enter second grade: "))
total_classes = int(input("Enter total number of classes: "))
absences = int(input("Enter number of missed classes: "))

average_grade = (grade1 + grade2) / 2
attendance = ((total_classes - absences) / total_classes) * 100


# Student needs at least an average of 6 and attendance rate of 80 to pass the class. Did they? (NO USING CONDITIONAL OPS)
if (average_grade < 6):
    print("YOU FAILED, REASON: GRADE TOO LOW")
elif (attendance < 80):
    print("YOU FAILED, REASON: ATTENDANCE TOO LOW")
else:
    print("YOU IN!")


# Alt soln with nested if
if (average_grade >= 6):
    if (attendance >= 80):
        print("YOU IN!")
    else:
        print("YOU FAILED")
else:
    print("YOU FAILED")


# Do more conditional checking (failed due to x, y, or x and y) and this time use AND, OR, NOT
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