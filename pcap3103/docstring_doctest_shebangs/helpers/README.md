# Docstrings

Docstrings is a comment like section starts with `'''` but unlike real comment its not ignored by interpreter. instead it uses save in __doc__ variable.


# Doctest

We add test and its result in REPL format inside docstrings. see math.py.  and then if you run `python3.7 -m doctest helpers/src/helpers/math.py`. if there are no errors then it means your code is running fine.


```
cd ~/project_dir/helpers
pip3.7 install --editable . #this will let you edit and see changes quickly instead of building code again and again
```

```
python3.7
import helpers
helpers.__doc__

```

# Shebang

To make our script executable we need to change its permission and add shebang to it.

`#!/usr/bin/env python`

`chmod +x ~/project_dir/main.py`

`#!/home/cloud_user/.pyenv/versions/3.7.6/bin/python`

Even though if our running environment is python2.7 but when we run it with python command and there is shebang in the file it will run according to shebang version instead of newly added version