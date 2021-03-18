from helpers import *
from helpers import extract_lower #we need to explicity get as it is not set by __all__ variable
import extras


print(f"Uppercase Letters: {extract_upper(extras.name)}")
print(f"Lowercase Letters: {extract_lower(extras.name)}")
