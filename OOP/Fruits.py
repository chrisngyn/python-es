class Fruit:
    def __init__(self, fruit, color):
        self.fruit = fruit
        self.color = color

    def show(self):
        print("Fruit is:", self.fruit)
        print("Color is " + self.color)

Apple = Fruit("Apple", "red")
Apple.show()