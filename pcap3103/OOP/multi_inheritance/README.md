# Single and Multiple inhertance

## Two important thing

1. Method resolution order
2. **kwargs

### Method Resolution Order

When inheriting from multiple class its order goes from left to right like `AmphibiousVehicle(Car, Boat)`. 
In this case first it will go for Car constructor then Boat constructor then Object.
You can check this using
```
av = AmphibiousVehicle('4-cylinder')
av.__mro__ #this will list the resolution order for you
```

### **kwargs 

It is used as positional named arguments. we specify **kwargs as last argument and pass as named argument.
so even when calling if you miss some argument then it will be skipped. 



