# __init__() is your constructor
# self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class

class Triangle:
    def __init__(self, length, width):     # constructor
      self.length = length                 # assigning field values
      self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def set_length(self, new_length):
        self.length = new_length

    def set_width(self, new_width):
        self.width = new_width

    def area(self):
        return (self.length * self.width) / 2

    def greater_area(self, Triangle):
        if self.area() < Triangle.area():
            return "arg triangle has greater area"
        else:
            return "self triangle has greater area"