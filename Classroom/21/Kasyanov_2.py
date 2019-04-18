from math import sin, pi
def f(x):
	return 2*x-3*sin(2*x)-1
mn=-5
mx=5
e=0.00001

minint = -20
maxint = -20-2*pi
while abs(maxint-minint)>=e:
	if f(minint>f(maxint))