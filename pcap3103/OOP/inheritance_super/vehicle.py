class Vehicle:
    '''
    Vehicle is a device that can be used to travel
    '''

    default_tire = 'tire'

    def __init__(self, distance_traveled=0, unit='miles'):
        self.distance_traveled = distance_traveled
        self.unit = unit

    # @classmethod
    # def bicycle(cls, tires=None):
    #     if not tires:
    #         tires = [cls.default_tire, cls.default_tire]
    #     return cls(None, tires)

    
    def description(self):
        return f'A {self.__class__.__name__} that has traveled {self.distance_traveled} {self.unit}'
    

    

