from math import sin, tan
"""Вычислить значение функции"""


def f(x):
    if x >= 0:
        return sin(x**2+x**0.5)
    # elif -1 < x <= 0:
    #     y = x**2**0.5**(1/3)+sin(x**3)
    #     return y
    else:
        return x**2*tan(x**(1./3))


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
        9999,
        -10.02,
        "test_to_error",
        3
    ]
    for i in list_of_tests:
        try:
            print("При x=", i, " f(x)=", f(i), sep="")
        except:

            print("Test error")


tests()
try_func()
