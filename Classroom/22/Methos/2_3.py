
def chord_metod(base, exp=2, it=20):
    def f(x):
        return x**exp - base
    def df(x):
        return exp*(x**(exp-1))
    x1 = base / float(exp**2)
    xnp = x1
    xn = 0
    for n in range(it):
        xn = xnp - ((f(xnp)/df(xnp)))
        xnp = xn
    return xn

print(chord_metod(2, 2))