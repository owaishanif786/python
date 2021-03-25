import sys
import random

try:
    print(f'First argument {sys.argv[1]}')
    args = sys.argv
    random.shuffle(args)
    print(f'Random arguments {args[0]}')
except (IndexError, KeyError) as err: #Note you can group multiple exception types in same block
    print(f'Error: no arguments please provide at least one .({err})')
except NameError:
    print(f'Error: Random module not loaded')
else:
    print(f'Everything was fine') #this will only if there was no exception
finally:
    print('Finally is running') #this section will always run