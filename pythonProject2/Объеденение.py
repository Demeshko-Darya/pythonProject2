import random

a = {random.randint(1, 20) for i in range(10)}
b = {random.randint(1, 20) for j in range(10)}
print(a)
print(b)
c = a.copy()
c.update(b)
print(c)
