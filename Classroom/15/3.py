'''3.Даны действительные числа x1, ..., x8. Получить действительную квадратную
матрицу порядка 8:'''
def printarray(c=[]):
	for x in range(len(c)):
		for i in range(len(c[0])):
			print("{:6d}".format(c[x][i]),end="")
		print("")
def create(m=0,n="Err",r=0):
	if(n=="Err"):
		n=m
	g=[]
	if r==0:   
		for i in range(m):
			m1=[]
			for j in range(n):
				m1.append(0)
			g.append(m1)
	else:
		from random import randint
		for i in range(m):
			m1=[]
			for j in range(n):
				m1.append(randint(0,9))
			g.append(m1)   
	return g	
def arrtodigit(a=[]):
	for i in range(len(a)):
		a[i]=float(a[i])
		if a[i]%1==0:
			a[i]=int(a[i])
	return a
b=create(8)
b[0]=arrtodigit(input("Введите первый ряд:\n").split())
for i in range(1,len(b)):
	for j in range(len(b)):
		b[i][j]=b[0][j]**i
print("a)")
printarray(b)
for i in range(1,len(b)):
	for j in range(len(b)):
		b[i][j]=b[0][j]**(i-1)
print("b)")
printarray(b)