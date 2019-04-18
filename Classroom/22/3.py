from math import cos
def f(x):
	#return 2*x**3-10*x +20*cos(5*x)

	return x**0.5

def lenth(f,a,b,e):
    l=0
    while a<=b:
        l+=((f(a)-f(a+e))**2+e**2)**0.5
        a=a+e
    return l
#a=lenth(f,int(ar[0]),int(ar[1]),float(ar[2]))
a=lenth(f,0,20,0.0001)
print(round(a,3))
