# Assertions

assertion will trigger exception if it get false in evaluation.

```python
>>> assert False, 'errrrrr'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: errrrrr
>>> assert True, 'errrrrr'

>>> assert len([1,2,3]) >= 2, 'shorter length'
>>> assert len([1]) >= 2, 'shorter length'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: shorter length
```

## Assertion is a debugging Tool

While running you can skip assertion statements by passing `-O` argument or `-OO` if you want to remove docstrings.

