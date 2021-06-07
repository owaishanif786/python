
# *args means any number of arguments  with be store in variable. 
#called variadic function
def inspect(func):

    def wrapped_func(*args, **kwargs):
        print(f"Running {func.__name__}")
        val = func(*args, **kwargs)
        print(f"Result {val}")
        return val
    return wrapped_func #for decorator it must return a function


@inspect #'combine' will be passed to 'inspect' function
def combine(a, b):
    return a+b

# >>> inspect(combine, 1,2)

class User:
    base_url = 'https://example.com/api'

    def __init__(self, first_name, last_name):
        self.first_name  = first_name
        self.last_name = last_name
    
    @classmethod
    def query(cls, query_string): #first variable will be class it-self but not self variable. we usually use cls as convention
        return cls.base_url + '?' + query_string
    
    @staticmethod #this method is not affected by class state
    def name():
        return 'big bang'

    @property #defining some method resulst as property 
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    


