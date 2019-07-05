from queue import ExtendibleArray
from datetime import datetime
from sys import getsizeof

line = ExtendibleArray()
now = datetime.now()
for i in range(1000000):
    line.add(i)
print(getsizeof(line.getlist()))
then = datetime.now()
print(then - now)

items = []
now = datetime.now()
for i in range(1000000):
    items.append(i)
print(getsizeof(list(filter(None.__ne__, items))))
then = datetime.now()
print(then - now)
