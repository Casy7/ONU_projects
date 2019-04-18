def f(x):
	return x**2-5*x
def chord_metod(f, x0, x1, e, max_iterations=100):
	


	for _ in range(max_iterations):
		if abs(f(x1)) < e:
			return x1
		x2 = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
		x0,  x1  = x1,  x2

chord_metod(f,)