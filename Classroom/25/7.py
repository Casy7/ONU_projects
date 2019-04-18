"""Вычислить периметр и площадь квадрата, вписанного
в окружность заданного радиуса."""


def square(r):
    try:

        a = (2*r)/2**0.5
        p = 4*a
        s = a**2

        print("Площадь:", s)
        print("Периметр:", p, "\n")
        return s, p
    except:
        print("Ошибка\n")
        return None


square(0)
square(6)
square(8)
square(9.25)
square(1000.0)
