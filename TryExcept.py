# Take the student grades program and validate everything. Make it smooth af.

# Validating inputs. Grade is 0-10 but accepts any #. Absences can be greater than total. Total # of class can be negative.
# Not only do we need to validation the data CONTENTS, but also the data TYPE. cause someone can enter a STRING!!

data_validation = False
while (data_validation == False):
    try:
        grade1 = float(input("Enter first grade: "))                # String protection
    except:
        print("Value not allowed!")
        continue
    if (grade1 < 0 or grade1 > 10):
        print("Value not allowed!")
    else:
        data_validation = True
        continue

data_validation = False
while (data_validation == False):
    try:
        grade2 = float(input("Enter second grade: "))                # String protection
    except:
        print("Value not allowed!")
        continue
    if (grade2 < 0 or grade2 > 10):
        print("Value not allowed!")
    else:
        data_validation = True
        continue

data_validation = False

while (data_validation == False):
    try:
        total_classes = int(input("Enter number of total classes: "))
    except:
        print("Value not allowed!")
        continue
    if (total_classes <= 0):
        print("Value not allowed!")
    else:
        data_validation = True
        continue                                                    # move onto next iteration which will pass

data_validation = False

while (data_validation == False):
    try:
        absences = int(input("Enter number of absences: "))
    except:
        print("Value not allowed!")
        continue
    if (absences < 0 or absences > total_classes):
        print("Value not allowed!")
    else:
        data_validation = True
        continue

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