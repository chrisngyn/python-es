# Create a program to calculate the BMI of a person. Ask for height in metres and weight in kilograms.
# <= 18.5 - underweight
# > 18.5 & <= 24.9 - normal
# > 24.9 & <= 29.9 - overweight
# >= 30 - obese
height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight in kilograms: "))

BMI = round(weight / (height**2), 2)

if (BMI <= 18.5):
    print("Your BMI is:", BMI, "so you are UNDERWEIGHT.")
elif (BMI <= 24.9):
    print("Your BMI is:", BMI, "so you are NORMAL.")
elif (BMI <= 29.9):
    print("Your BMI is:", BMI, "so you are OVERWEIGHT.")
else:
    print("Your BMI is:", BMI, "so you are OBESE.")