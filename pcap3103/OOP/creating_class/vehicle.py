class Vehicle:
    """
    Vehicle class 
    """
    def __init__(self, engine, tyres):
        """
        Vehicle constructor
        """
        self.engine = engine
        self.tyres = tyres
    
    def description(self):
        """
        Vehicle custom method
        """
        print(f'Vehicle with engine: {self.engine} and tyres: {self.tyres}')
    
    
    