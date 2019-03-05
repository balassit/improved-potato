import time
from itertools import zip_longest

first = [0, 1]
second = [1, 2, 3]

start = time.time()
result = 0
longest = len(first) if len(first) > len(second) else len(second)
for i, (x, y) in enumerate(zip_longest(reversed(first), reversed(second))):
    if x is None:
        x = 0
    elif y is None:
        y = 0
    result += (x + y) * (10 ** (longest - 1 - i))
end = time.time()
print(result)
print(end - start)
# result = list(zip(first, second))


# print(*result)
