class Car:
    """
    Docstring describing car class
    """

    def __init__(self, model, cc, tires):
        self.model = model
        self.cc = cc
        self.tires = tires
    
    def description(self):
        print(f"{self.model} {self.cc} {self.tires}")

    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0

# if __name__ == '__main__':
#     c = Car('honda', 2000, )
#     c.description()

