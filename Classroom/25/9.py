"""Для цилиндра радиусом R и высотой H напишите программу вычисления его
площади и объема."""
from math import pi


def cylinder(r, h):

    try:
        v = pi*r**2*h
        s = 2*pi*r*h+2*pi*r**2
        print("Площадь поверхности цилиндра:", s)
        print("Объём цилиндра:", v, "\n")
        return s, v
    except:
        print("Ошибка\n")
        return None


cylinder(0, 0)
cylinder("радиус", 6756)
cylinder(4, 6)
cylinder(9.25, 15)
cylinder(1000.0, 2000)
