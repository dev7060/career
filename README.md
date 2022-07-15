
   + -- Calci
        + -- __ init __.py
        + -- arnav.py
        + -- sharad.py
   + -- sc.py
   

sc.py
```python
import Calci

print(Calci.arnav)
print(Calci.sharad)

print(Calci.add(5, 5))
print(Calci.multiply(5, 5))

print(Calci.arnav.add(5, 5))
print(Calci.sharad.multiply(5, 5))
```


__ init __.py
```python
from .arnav import add
from .sharad import multiply
```

arnav.py
```python
def add(x, y):
	return x+y
```

sharad.py
```python
def multiply(x, y):
	return x*y
```

To see the imported modules

sc.py
```python
import Calci

print(Calci.add(5, 5))
print(Calci.multiply(5, 5))

print(Calci.arnav.add(5, 5))
print(Calci.sharad.multiply(5, 5))

import sys

for i in sys.modules:
	print(i)
```


---
https://docs.python.org/3/tutorial/inputoutput.html
> In text files (those opened without a b in the mode string), only seeks relative to the beginning of the file are allowed (the exception being seeking to the very file end with seek(0, 2)) and the only valid offset values are those returned from the f.tell(), or zero. Any other offset value produces undefined behaviour.

https://pynative.com/python-file-seek/
> If your using seek() function in text files (those opened without a b in the access mode), only seeks relative to the beginning of the file are allowed. If you try to move the file handle from the current position you’ll get an io.UnsupportedOperation: can't do nonzero cur-relative seeks error. So open the file in binary mode if you want to move the file pointer ahead or behind from the current position
