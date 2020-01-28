# Create a program that prompts a user for a circle radius and output circumference and area

import math

radius = float(input("Enter radius: ")) # don't forget to cast.
print ("Circumference is: ", math.pi * radius * 2)
print ("Area is: ", (math.pi * (radius ** 2)))