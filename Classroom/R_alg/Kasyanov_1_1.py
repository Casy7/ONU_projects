from math import sin
"""Вычислить значение функции"""


def f(x):
    if x > 0:
        return x**5
    elif -1 < x <= 0:
        y = x**2**0.5**(1/3)+sin(x**3)
        return y
    else:
        return 10-x


def try_func():
    while True:
        try:
            x = float(input("Введите x: "))
            print("При x=", x, " f(x)=", f(x), sep="")
        except:
            print("Input error")


def tests():
    list_of_tests = [
        12,
        10,
        3
    ]
    for i in list_of_tests:
        try:
            print("При x=", i, " f(x)=", f(i), sep="")
        except:

            print("Test error")


tests()
try_func()
