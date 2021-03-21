class Vehicle:
    '''
    Vehicle models with tyres and engine
    '''

    default_tire = 'tire' #class level variable

    def __init__(self,engine, tires):
        '''
        Vehcile class default constructor
        '''
        self.engine = engine
        self.tires = tires


    @classmethod
    def bicycle(cls, tires=None):
        if not tires:
            tires = [cls.default_tire, cls.default_tire]
        return cls(None, tires)
    
    def description(self):
        print(f'Car with engin: {self.engine} and tires: {self.tires}')
    
