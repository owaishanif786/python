from car import Car
from boat import Boat

class AmphibiousVehicle(Car, Boat):

    def __init__(self, engine, tires=None, distance_traveled=0, unit='miles'):
        super().__init__(engine=engine, tires=tires, distance_traveled=distance_traveled, unit=unit )
        self.boat_type = 'motor'
    
    def travel(self, land_distance=0, water_distance=0):
        super().drive(land_distance)
        super().voyage(water_distance)
    
