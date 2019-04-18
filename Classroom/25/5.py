"""По длинам двух сторон треугольника и углу (в градусах)
между ними вычислить длину третьей стороны и площадь этого треугольника."""
from math import cos, radians, sin


def theo_cos(a, b, alphagrad=None, alpharad=None):

    try:
        if alphagrad is not None:
            alpha = radians(alphagrad)
        elif alpharad is not None:
            alpha = alpharad

        c = (a**2+b**2-2*a*b*cos(alpha))**0.5
        s = 1/2*a*b*sin(alpha)
        print("Сторона a=", a, ", b=", b, ", c=", c, sep="")
        print("Площадь:", s, "\n")

        return c, s
    except:
        print("Ошибка")
        return None


theo_cos(3, 4, 90)
theo_cos(6, 8, alpharad=2)
theo_cos(1000.0, 2000.0)
