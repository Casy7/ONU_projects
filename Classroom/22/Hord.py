from math import cos
def f(x):
	return x**2-2*cos(x)-3
def minf(a,b,e,f):
	mi = 999999
	while(a<=b):
		if f(mi)>f(a):
			mi=a
		a+=e
		
	return f(mi)
def method(a,b,e):
	
