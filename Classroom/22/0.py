def f(x):
	return x**2-5*x-6
def HDM(a,b,e,f):
	arr=[]
	while(a<=b-e):
		if f((a+b)/2)*f(b)==0:
			if (a+b)/2==0:
				arr.append((a+b)/2)
				break
			else:
				arr.append(b)
				break
		elif f((a+b)/2)*f(b)<0:
			a=(a+b)/2
		else:
			b=(a+b)/2
	arr.append(a)
	return arr
print(HDM(-10,3,0.0001,f))
