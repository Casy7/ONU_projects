from math import cos
def f(x):
	#return 2*x**3-10*x +20*cos(5*x)

	return 5*x**3-15*x +30*cos(5*x)

def minf(a,b,e,f):
	mi = 999999
	while(a<=b):
		if f(mi)>f(a):
			mi=a
		a+=e
	return f(mi)
a=minf(0,3,0.0001,f)
print(round(a,3))
