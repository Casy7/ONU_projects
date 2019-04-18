"""Найти площадь кольца, внутренний радиус которого равен R1, а
внешний радиус равен R2."""
from math import pi


def circles(r1, r2):

    try:

        s1 = pi*r1**2
        s2 = pi*r2**2
        if r1 > r2:
            1/0
        s = s2 - s1
        print("Площадь:", s, "\n")
        return s
    except:
        print("Ошибка\n")
        return None


circles(3, 4)
circles(6, 8)
circles(8, 8)
circles(9, 8)
circles(1000.0, 2000.0)
