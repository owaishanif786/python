class Mapping:
    def __init__(self, iterable):
        self.item_list = []
        self.__update = update(iterable) #setting __update on the class and it will be available in child class but not the update method it self

    def update(self, iterable):
        for item in terable:
            self.item_list.append(item)

    __update = update #storing private copy of update


class SubMapping(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.item_list.append(item)

    def printSomething(self):
        print("Printing Something")

    __update = printSomething