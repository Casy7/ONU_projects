def f(x):
	return x**2-5*x-6
def HDM(
	a:"Начало отрезка, но котором есть точно один корень.",
	b:"Конец отрезка, но котором есть точно один корень.",
	e:"Точность нахождения коря уравнения.",
	f:"Приниммаемая функция."):
	"""Решение уравнения f(x)=0 методом половинного деления"""
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
	return round(arr[0],len(str(e))-2)
print(HDM(-10,3,0.0001,f))
