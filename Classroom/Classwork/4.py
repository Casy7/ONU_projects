x=0.0
y=0.0
while(True):
	x=float(input("Введите координату x:  "))
	y=float(input("Введите координату y:  "))
	if (x**2+y**2<=1 and x>=0) or (y>=x-1 and y<=1 and x>=0):
		print("Точка принадлежит области")
	else:
		print("Точка не принадлежит области")