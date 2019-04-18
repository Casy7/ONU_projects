#Модуль для работы с массивами
#TODO нужно больше функций!
def chord(
	a:"Начало отрезка, но котором есть точно один корень.",
	b:"Конец отрезка, но котором есть точно один корень.",
	e:"Точность нахождения коря уравнения.",
	f:"Приниммаемая функция."):
	"""решение уравнения f(x) =0 методом хорд (секущих)"""
	e=int(1/e)
	for i in range(a*100,b*100):
		x1 = a
		x2 = b
		if f(i)>0 and f(i)>x2:
			x2 = i
		elif f(i)<0 and f(i)<x1:
			x2 = i
		x1/=100
		x2/=100
	for i in range(e):
		y1=f(x1)
		y2=f(x2)
		b = (x1*y2-x2*y1)/(x1-x2)
		k=(y1-b)/x1
		x=-b/k
		x1=x
	return round(x,len(str(e)))
def hdm(
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
def sq(
	f:"Функция первой линии",
	g:"Функция второй линии"):
	"""Нахождение площади ограниченной линиями фигуры"""
	def HDM(a,b,e,f):
		arr=[]
		for i in range(a,b):
			a=i
			b=i+1
			c = 0
			while(a<=b-e and c<1000):
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
	def e3(x):
		return f(x)-g(x)
	def sq(f,a,b,e):
		s=0
		while a<=b-e:
			s+=f(a)*e
			a=a+e
		return s
	y=HDM(-20,20,0.001,e3)
	print(y)
	if(len(y))==2:
		return abs(sq(f,y[0],y[1],0.001)-sq(g,y[0],y[1],0.001))
	else:
		return "Фигура не замкнута!"
def simpleSq(
	a:"Начало промежутка.",
	b:"Конец промежутка.",
	e:"Точность.",
	f:"Приниммаемая функция."):
		"""Нахождение площади под функцией на промежутке."""
		s=0
		while a<=b-e:
			s+=f(a)*e
			a=a+e
		return s
def lenth(
	a:"Начало промежутка.",
	b:"Конец промежутка.",
	e:"Точность.",
	f:"Приниммаемая функция."):
	"""Нахождение длины функции на промежутке"""
	l=0
	while a<=b:
		l+=((f(a)-f(a+e))**2+e**2)**0.5
		a=a+e
	return round(l,len(str(e)))
def minimum(
	a:"Начало промежутка.",
	b:"Конец промежутка.",
	e:"Точность.",
	f:"Приниммаемая функция."):
	"""Минимальное значение на промежутке"""
	mi = 999999
	while(a<=b):
		if f(mi)>f(a):
			mi=a
		a+=e
	return round(f(mi),len(str(e)))
def maximum(
	a:"Начало промежутка.",
	b:"Конец промежутка.",
	e:"Точность.",
	f:"Приниммаемая функция."):
	"""Максимальное значение на промежутке"""
	ma = -999999
	while(a<=b):
		if f(ma)<f(a):
			ma=a
		a+=e
	return round(f(ma),len(str(e)))
