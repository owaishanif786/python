# Raising Exceptions

```python
>>> err = Exception("something went wrong") 
>>> err
Exception('something went wrong')
>>> str(err)
'something went wrong'
>>> dir(err)
['__cause__', '__class__', '__context__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__suppress_context__', '__traceback__', 'args', 'with_traceback']
```

Creating Exception doesn't stop execution. The Exception class is the parent class for most exceptions, and we can see these by using Exceptin.__subclasses__()

The child classes of Exception class can be listed by `.__subclasses()`
`Exception.__subclasses()`

```python
>>> Exception.__subclasses__()
[<class 'TypeError'>, <class 'StopAsyncIteration'>, <class 'StopIteration'>, <class 'ImportError'>, <class 'OSError'>, <class 'EOFError'>, <class 'RuntimeError'>, <class 'NameError'>, <class 'AttributeError'>, <class 'SyntaxError'>, <class 'LookupError'>, <class 'ValueError'>, <class 'AssertionError'>, <class 'ArithmeticError'>, <class 'SystemError'>, <class 'ReferenceError'>, <class 'MemoryError'>, <class 'BufferError'>, <class 'Warning'>, <class 'locale.Error'>]
```

To list parent classes of `Exception` we can use `__bases__` property.

```python
>>> Exception.__subclasses__()
[<class 'TypeError'>, <class 'StopAsyncIteration'>, <class 'StopIteration'>, <class 'ImportError'>, <class 'OSError'>, <class 'EOFError'>, <class 'RuntimeError'>, <class 'NameError'>, <class 'AttributeError'>, <class 'SyntaxError'>, <class 'LookupError'>, <class 'ValueError'>, <class 'AssertionError'>, <class 'ArithmeticError'>, <class 'SystemError'>, <class 'ReferenceError'>, <class 'MemoryError'>, <class 'BufferError'>, <class 'Warning'>, <class 'locale.Error'>]
>>> Exception.__bases__
(<class 'BaseException'>,)
>>> BaseException.__bases__
(<class 'object'>,)
>>> BaseException.__subclasses__()
[<class 'Exception'>, <class 'GeneratorExit'>, <class 'SystemExit'>, <class 'KeyboardInterrupt'>]
```

Object is parent of BaseException and BaseException is parent of Exception.
object>BaseException>Exception

```python
>>> Exception.__bases__
(<class 'BaseException'>,)
>>> BaseException.__bases__
(<class 'object'>,)
>>> BaseException.__subclasses__()
[<class 'Exception'>, <class 'GeneratorExit'>, <class 'SystemExit'>, <class 'KeyboardInterrupt'>]
```

```shell
python3.7 main.py 
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    raise Exception('not enough arguments')
Exception: not enough arguments
```

```shell
python3.7 main.py lilWolf
Name is lilWolf
```
