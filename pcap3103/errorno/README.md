# errno

errno is an error code than can help use handle to do better exception handling.

```python
import errno

try:
    f = open('fake.txt', 'r')
except OSError as err:
    if err.errno == errno.ENOENT: #ENOENT stands for ERROR NO ENTITY in case file not found
        print("File not found")
    elif err.errno == errno.EACCES:
        print("Can't access")
```

we can also derive errno from errorcode

```python
import errno
import os

try:
    f = open('fake.txt', 'r')
except OSError as err:
    if err.errno == errno.ENOENT:
        print("File not found")
    elif err.errno == errno.EACCES:
        print(f"[Errno {err.errno} ({errno.errorcode[err.errno]})] {os.strerror(err.errno)}")
```
