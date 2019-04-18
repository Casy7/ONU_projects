"""Вычислить сумму членов геометрической прогрессии, если
известен ее первый член, знаменатель и число членов прогрессии."""


def progression(
        b1: "первый член",
        q: "знаменатель",
        n: "число членов прогрессии"):
    try:
        n = int(n)
        res_sum = b1*(q**n-1)/(q-1)
        print("Сумма ", n, " первых членов прогрессии = ",
              res_sum, "\n", sep="")
        return res_sum
    except:
        print("Ошибка\n")
        return None


progression(1, 1, 5)
progression("h", 6756, 0)
progression(2, 2, 4)
progression(9.25, 15, 2)
progression(1000.0, 2000, 10.5)
