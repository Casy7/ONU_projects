def f(x):
	return x**2-5*x-6
def HDM(a,b,e,f):
	arr=[]
	for i in range(a,b):
		a=i
		b=i+1
		c = 0
		while(a<=b-e and c<10000):
			h=0
			if f((a+b)/2)*f(b)==0:
				if (a+b)/2==0:
					arr.append((a+b)/2)
					break
				else:
					arr.append(b)
					break
			elif f((a+b)/2)*f(b)<0:
				a=(a+b)/2
				h=1
			elif f(a)*f((a+b)/2)<0:
				b=(a+b)/2
				h=1
			c+=1
		if(h==1):
			arr.append(a)
	return arr
print(HDM(-10,7,0.0001,f))