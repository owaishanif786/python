# FILE IO

```python
f = open('filename.txt', 'mode')
```

## Modes

```text
'r' - Opens the file for reading, which is the default mode
'w' - Opens the file for writing, while removing the existing content (truncating the file)
'x' - Opens the file to create it, failing if the file already exists
'a' - Opens the file for writing without truncating, appending any new writes to the end of the file
'b' - Opens the file in binary mode, in which the file expects to write and return bytes objects
't' - Opens the file in text mode, the default mode, where the object expects to write and return strings
```

## Methods

- .write will write indiviudal files
- .read
- .seek
- .writelines

`open` method is used to read/write files in python.

**Note: Always close the file after opening it.**

### The `with` Statement

with statement will automatically close  the file after block will end.
