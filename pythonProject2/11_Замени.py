import random

a = [random.randint(1, 100) for i in range(20)]
print(a)
b = int(input("какое число заменить? : "))
c = int(input("на какое число заменить? : "))
for j in range(len(a)):
    if a[j] == b:
        a[j] = c
print(a)
