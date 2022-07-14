
   + -- Calci
        + -- __ init __.py
        + -- arnav.py
        + -- sharad.py
   + -- sc.py
   

sc.py
```python
import Calci

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


__ init __.py -> wont be compiled individually as it will search for the parent package (because of .)

Too see the imported modules

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

