from helpers import *
from helpers import extract_lower #we need to explicity get as it is not set by __all__ variable
from helpers import _sum

import extras


print(f"Uppercase Letters: {extract_upper(extras.name)}")
print(f"Lowercase Letters: {extract_lower(extras.name)}")
print(f"SUM 1+2: {_sum(1,2)}")