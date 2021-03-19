# Package in python

Modules files grouped together. we keep __init__.py file inside folder to declare that folder as package.

then simply 
`from helpers.file import func_name`

## Purpose of `__init__.py`

Whenever moudle is access from package this `__init__.py` will be ran first. any code inside that file will be triggered.
Also we can use `__all__` to expose specific entities.

