class ExampleError(Exception):
    pass

def bad_function():
    raise ExampleError('this is a message', 1, 2)

try:
    bad_function()
except ExampleError as err:
    message, x, y, *others = err.args
    print(f'[I] {message}')
    print(f'[I] Others: {others}')