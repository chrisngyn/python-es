from Car import *

# you could just have this in the same file, too.
# or you can just import and use the __init__() method as per usual.

ChrisCar = Car("Tesla", "2016", 40000)
print(ChrisCar.car_model, ChrisCar.year_made)

# both of these work to use a class method
# {object}.method, or Class.method(object)
print(ChrisCar.year())
print(Car.year(ChrisCar))
print(ChrisCar.value())
print()

# put those docstrings to use.
help(Car)