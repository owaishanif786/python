# Inspecting Objects

There are few functions that can help us in debugging by analyzing objects.

- `.__bases__` will tell us about parent class
- `.__subclasses__()` will tell us about child class
- `dir()` will tell us the structure of object
- `hasattr()` will tell us the whether attribute exits on object or not
- `issubclass()` will tell us whether one class is child of second class
- `isinstance()` will tell if the instance is from the specified class
- `__dict__` will tell us about customizable(writeable) properties
- `type` will tell us the class that was used to create the object.
- `str` will tell us about string representable form using __str__ property

To check the parent class/classes of a class use `.__bases__` i.e

```shell
python -i amphibious_vehicle.py 
>>> AmphibiousVehicle.__bases__
(<class 'car.Car'>, <class 'boat.Boat'>)
```

To check the child class/classes of a class use `.__subclasses__()` i.e

```python
>>> Vehicle.__subclasses__()
[<class 'car.Car'>, <class 'boat.Boat'>]
```

`dir` will tell us the structure of object. some special attributes still wont be visible like `__bases__`

```python
>>> dir(AmphibiousVehicle)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'default_tire', 'description', 'drive', 'travel', 'voyage']
```

The `hasattr(className, 'property_to_check')` method let us know if attribute exists on class/object. For class it will tell us the class level attributes. On object it will tell us the Object level attributes.

```shell
>>> hasattr(Boat, 'boat_type')
False
>>> hasattr(boat, 'boat_type') #here notice the different its giving true on instance but false on Class. 
True
>>> 
>>> hasattr(Car, 'default_tire') #here notice even though its class still its giving true because we defined default_tire as classful attributes 
True
```

`issubclass(child_class, parent_class)` tells that if first class is the child of second class provided in parameter.

```python
>>> issubclass(Car, Vehicle)
True
>>> issubclass(Vehicle, Boat)
False
```

`isinstance(instance_name, class_name)` this method will tell us whether instance_name is the child of class_name. This method will return true even instance is of class' subclass.

```python
>>> water_car = AmphibiousVehicle('4-cylinder')
>>> isinstance(water_car, AmphibiousVehicle)
True
>>> isinstance(water_car, Boat) #here Boat is Parent class of AmphibiousVehicle but still its returning true.
True
```

`__dict__` will give us dictionary like object. which will contain all custom(writeable) attributes.

```python
>>> water_car.__dict__
{'distance_traveled': 0, 'unit': 'miles', 'boat_type': 'motor', 'engine': '4-cylinder', 'tires': ['tire', 'tire', 'tire', 'tire']}
>>> AmphibiousVehicle.__dict__
mappingproxy({'__module__': 'amphibious_vehicle', '__init__': <function AmphibiousVehicle.__init__ at 0x7fe4a93f0830>, 'travel': <function AmphibiousVehicle.travel at 0x7fe4a93f8050>, '__doc__': None})
```

`type` will tell us the class that was used to create the object. The usualy output of class type will be `<class '__moduleName__.ClassName'>` but if something is ran from main file it will be like. `<class '__main__.ClassName'>`. You can also check by Object module property by running. `Object.__module__`

```python
>>> type(water_car)
<class 'amphibious_vehicle.AmphibiousVehicle'>

>>> type(boat)
<class 'boat.Boat'>

>>> type(vehicle)
<class '__main__.Vehicle'>

>>> Boat.__module__
'boat'
```

## Customizing Object Information with __str__

```python
>>> str(boat)
'<boat.Boat object at 0x7f8da00e6910>'
```

Update amphibious_vehicle class code with override __str__ property

```python
from car import Car
from boat import Boat

class AmphibiousVehicle(Car, Boat):

    def __init__(self, engine, tires=None, distance_traveled=0, unit='miles'):
        super().__init__(engine=engine, tires=tires, distance_traveled=distance_traveled, unit=unit )
        self.boat_type = 'motor'
    
    def travel(self, land_distance=0, water_distance=0):
        super().drive(land_distance)
        super().voyage(water_distance)
    
    def __str__(self):
        return f'<{self.__class__.__name__} {self.__dict__}>'

if __name__  == '__main__':
    water_car = AmphibiousVehicle('4-cylinder')
    print(water_car)
```

Run and check the output. `python amphibious_vehicle.py`

```python
<AmphibiousVehicle {'distance_traveled': 0, 'unit': 'miles', 'boat_type': 'motor', 'engine': '4-cylinder', 'tires': ['tire', 'tire', 'tire', 'tire']}>
```
