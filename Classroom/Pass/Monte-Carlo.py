from random import random
from random import randint


def f(x):
    return x**2


d = 0
for i in range(100000):
    x = random()
    y = random()
    if y > f(x):
        d += 1
print(1-d/100000)

number = 100000
d = 0
for i in range(number):
    x = random()
    y = randint(0, int(x*10000))/10000
    if y > f(x):
        d += 1
print(d/number*2)
