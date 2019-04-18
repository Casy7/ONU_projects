"""Для конуса радиусом R и высотой H напишите
программу вычисления его объема."""
from math import pi


def cone(r, h):

    try:
        v = 1/3*pi*r**2*h
        print("Объём конуса:", v, "\n")
        return v
    except:
        print("Ошибка\n")
        return None


cone(0, 0)
cone("радиус", 6756)
cone(8, 6)
cone(9.25, 15)
cone(1000.0, 2000)
