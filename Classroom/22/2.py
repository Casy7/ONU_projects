from math import cos
def f(x):
	#return 2*x**3-10*x +20*cos(5*x)

	return 5*x**3-15*x +30*cos(5*x)

def HDM(a,b,e,f):
	mi = 999999
	ma = -999999
	while(a<=b):
		if f(ma)<f(a):
			ma=a
		if f(mi)>f(a):
			mi=a
		a+=e
	return [f(mi), f(ma)]
a=HDM(0,3,0.0001,f)
print(round(a[0],3),"; ",round(a[1],3),sep="")
