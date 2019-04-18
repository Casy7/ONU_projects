"""Вычислить сумму членов арифметической прогрессии, если известен ее
первый член, разность и число членов прогрессии."""


def progression(
        a1: "первый член",
        d: "разность",
        n: "число членов прогрессии"):
    try:
        n = int(n)
        res_sum = n*(a1+d*(n-1))/2
        print("Сумма ", n, " первых членов прогрессии = ",
              res_sum, "\n", sep="")
        return res_sum
    except:
        print("Ошибка\n")
        return None


progression(1, 1, 5)
progression("h", 6756, 0)
progression(4, 6, 20)
progression(9.25, 15, 2)
progression(1000.0, 2000, 10.5)
