from helpers.math import sum, area #import module from specif package file
from helpers import variables #import full module from variables
import helpers #import full package
from helpers import *  #import all modules from packages

print(f"Sum: 3+3: {sum(3,3)}")
print(f"Area with radius 3: {area(variables.PIE, 3)}")


