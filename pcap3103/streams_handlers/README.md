# Using Predefined Stream handlers

In sys module we have stdin, stdout and stderr

The STDOUT, STDERR is writeable streams while STDIN is read only.

```python
>>> import sys
>>> sys.stdout.write("Testing\n")
Testing
8
>>> sys.stderr.write("ERROR\n")
ERROR
6
>>> sys.stdin.write("Something")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
io.UnsupportedOperation: not writable
>>> sys.stdin.readlines()
Testing
Testing
['Testing\n', 'Testing\n']
```

