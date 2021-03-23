from vehicle import Vehicle

class Boat(Vehicle):

    def __init__(self, boat_type='sail', distance_traveled=0, unit='miles', **kwargs):
        print(f'__init__ from Boat with distance_traveled: {distance_traveled} and {unit}')
        #pass values to constructor
        super().__init__(distance_traveled=distance_traveled, unit=unit, **kwargs)
        self.boat_type = boat_type
    
    def voyage(self, distance):
        self.distance_traveled += distance

    
    def description(self):
        inital = super().description()
        return f'{inital} using a {self.boat_type}'


