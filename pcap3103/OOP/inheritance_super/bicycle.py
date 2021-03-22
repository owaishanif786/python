from vehicle import Vehicle
#pass parent object from which you want to inheirt
class Bicycle(Vehicle):

    default_tire = 'tire'

    def __init__(self, tires=None, distance_traveled=0, unit='mile'):
        super().__init__(distance_traveled, unit)
        if not tires:
            #below default_tire property being access from parent. as we have it already available.
            tires = [self.default_tire, self.default_tire]
        self.tires = tires

    def description(self):
        inital = super().description()
        return f"{inital} on {len(self.tires)} tires"
    

if __name__ == '__main__':
    bike = Bicycle()
    print(bike.description())


# $ python -i bicycle.py
# >>> bike = Bicycle()
# >>> bike.tires
# custom_bike = Bicycle(['front-tire', 'back-tire'])
# custom_bike.tiresdist
# custom_bike.description()


