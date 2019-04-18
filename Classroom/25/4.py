"""Вычислить среднее арифметическое и среднее
геометрическое двух положительных чисел."""


def average(a, b):

    try:
        alg = (a+b)/2
        geo = (a*b)**0.5

        print("Числа: a=", a, ", b=", b, sep="")
        print("Среднее арифметическое:", alg)
        print("Среднее геометрическое:", geo, "\n")
        return alg, geo
    except:
        print("Ошибка")
        return None


average(3, 4)
average(6, 8)
average(1000.0, 2000.0)
