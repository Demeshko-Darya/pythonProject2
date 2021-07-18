import random

a = [random.randint(1, 10) for i in range(10)]
print(a)
b = int(input("введите число : "))
c = a.index(b)
print(str(b) + "в списке под номером" + str(c))
