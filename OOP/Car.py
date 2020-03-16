class Car:
    # this is a docstring, when you type help(Car) it will give a description of this file
    """A class that represents a car."""

    # initialization method, also known as a constructor. called every time a new instance of a class is made
    # the first argument is SELF, which is a reference
    def __init__(self, model, year, value):
        self.car_model = model # your fields
        self.year_made = year # more fields
        self.price = value # computes these fields from init constructor

    def year(self): # method
        # docstring.
        """Method to return the year a car was made."""
        return self.year_made

    def model(self): # more methods
        # docstring.
        """Method to return the car model."""
        return self.car_model

    def value(self):
        """Method to return the value of a car."""
        return self.price