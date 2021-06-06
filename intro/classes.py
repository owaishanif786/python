class Car:
    """
    Docstring describing car class
    """

    def __init__(self, model, cc):
        self.model = model
        self.cc = cc
    
    def description(self):
        print(f"{self.model} {self.cc}")


if __name__ == '__main__':
    c = Car('honda', 2000)
    c.description()

