from Car import * # if having trouble with imports, right click on directory, Mark Directory As > Source Root

# you could just have this in the same file, too.
# or you can just import and use the __init__() method as per usual.

ChrisCar = Car("Tesla", "2016", 40000) # instance of Car class
print(ChrisCar.car_model, ChrisCar.year_made)

# both of these work to use a class method
# {object}.method, or Class.method(object)
print(ChrisCar.year())
print(Car.year(ChrisCar))
print(ChrisCar.value())
print(ChrisCar.ping())
print()

# put those docstrings to use.
help(Car)