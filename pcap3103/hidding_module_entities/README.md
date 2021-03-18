`__all__` allows us to specify which entities i.e functions variables to expose/hide. when user will `from helpers import *`.

Although it does not restrict but still it will help us what to export when using `* import`  syntax.

also if any entity starts with undercore `_` then it won't be used in other file. it would be kind of sudo hidden entities. but then again if will use explcit import i.e
from helpers `import _extract_upper` then it would be available

Similarly if any variable starts with undrescore `_` then it wont be aviable in other files using *. If we want to import so we need to import it explicity


So two ways to hide entities:
    1. use __all__ variable i.e __all__ = ['extract_upper']
    2. start entity with underscore `_` i.e _NAME = 'lil wolf'