# CodeDict

Made for brute-forcing

## Usage


```python
from codedict import Codes
```

**Traversing the dictionary**

```python
for psw in Codes.top1000():
    ...
```

**Dictionary concatenation**

```python
top1000 = Codes.top1000()
wpa = Codes.wpa()
for psw in top1000 + wpa:
    ...
```