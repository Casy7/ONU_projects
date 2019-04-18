'''1.Даны целые числа а1, a2, a3. Получить целочисленную матрицу
[bij] i, j = 1, 2, 3, для которой bij = ai - 3aj.'''
def arrtodigit(a=[]):
	for i in range(len(a)):
		a[i]=float(a[i])
		if a[i]%1==0:
			a[i]=int(a[i])
	return a
def printarray(c=[]):
	for x in range(len(c)):
		for i in range(len(c[0])):
			print("{:4d}".format(c[x][i]),end="")
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
a=arrtodigit(input("Введите числа i ").split())
b=create(3)
for i in range(len(b)):
	for j in range(len(b)):
		b[i][j]=a[i]-3*a[j]
printarray(b)