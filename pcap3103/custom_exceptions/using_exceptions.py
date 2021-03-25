import sys

from cli import main #importing main from __init__.py as that file runs code by default
from cli.errors import ArgumentError

try:
    main()
except ArgumentError as err:
    print(f'Error: {err}')
    sys.exit()
