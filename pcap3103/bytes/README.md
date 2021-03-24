# Bytes

```python
>>> bytes
<class 'bytes'>
```

To construct bytes there are two ways.

- starting with prefix b like `b'this is byte string'`
- using byte constructor `bytes('this is a byte string using constructor')`

Though it look like a string but actually its bytes. when something can have ascii representation in bytes then it can be represened as ascii.

```python
>>> bytes(10) #Create 10 bytes sequence
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' 

>>> my_bytes = b'this is a byte'

>>> my_bytes
b'this is a byte'

>>> my_bytes[0] #indexing of byte will return a number because indivaul byte will always be a number. here 116 is ascii vaule for 't' character
116

>>> my_bytes[0:1] #However if you want to get that character or sequence you can use slicing notation.
b't'

```

## bytearray

```python
>>> bytearray() #bytearray constructor
bytearray(b'')

>>> bytearray(10) #creating a sequence of 10 characters
bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

>>> bytearray(range(10))
bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t')

>>> bytearray(b'Bytes')
bytearray(b'Bytes')

>>> b_array = bytearray(10)
>>> b_array[0] = b'T' #we can't update byte-object on index format. we need to use slicing format to update 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object cannot be interpreted as an integer
>>> b_array[0:1] = b'T' #setting byte-object using slicing format
>>> b_array
bytearray(b'T\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> b_array[1] = 0x10 #setting hexadecmi/number using index format
>>> b_array
bytearray(b'T\x10\x00\x00\x00\x00\x00\x00\x00\x00')

>>> with open('names.txt', 'rb') as my_file:
...     my_file.readlines()
... 
[b'name1\n', b'name2\n', b'name3\n']

>>> my_file = open('names.txt', 'rb')
>>> b_array = bytearray(10)
>>> my_file.readinto(b_array)
10
>>> b_array
bytearray(b'name1\nname')

>>> my_file = open('names.txt', 'rb')
>>> b_array = bytearray(10)
>>> my_file.readinto(b_array) #loading file contents into byte array
10
>>> b_array
bytearray(b'name1\nname')
>>> new_b_array = bytearray(my_file.read(10))
>>> new_b_array
bytearray(b'2\nname3\n')
>>> bytearray(b'nix\nCyclop')
bytearray(b'nix\nCyclop')


```

### Difference between string and bytes

- String is immuatable(non-changeable) while bytes can be changed when created with 
