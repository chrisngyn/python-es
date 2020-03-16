from Triangle import *

triangle1 = Triangle(15, 8)
triangle2 = Triangle(20, 4)

print("Triangle1 length:", triangle1.length)
print("Triangle1 width:", triangle1.width)
print("Triangle1 area:", triangle1.area())
triangle1.set_length(50)
print("After setting triangle1 length to a new value, new area is:", triangle1.area())

print("--------------------------------------------------")

print(triangle1.area())
print(triangle2.area())
print(triangle1.greater_area(triangle2))
print(triangle2.greater_area(triangle1))

print("--------------------------------------------------")
help(Triangle)