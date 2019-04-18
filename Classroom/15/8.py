'''Дана действительная матрица размера n x m. Получить последовательность
b1, ..., bn, где bk - это'''
def printarray(c=[]):
	for x in range(len(c)):
		for i in range(len(c[0])):
			print("{:4d}".format(c[x][i]),end="")
		print("")
def create(m=0,n="Err",r=9):
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
				m1.append(randint(-r,r))
			g.append(m1)   
	return g	
m=int(input("Введите длину массива:  "))
n=int(input("Введите ширину массива:  "))
f=create(m,n)
printarray(f)
b1=[]
b2=[]
b3=[]
b4=[]
for i in range(m):
	b1.append("b"+str(i+1)+"="+str(max(f[i])))
	b2.append("b"+str(i+1)+"="+str(max(f[i])+min(f[i])))
	multiply=1
	nega=0
	for u in range(n):
		if (f[i][u])<0:
			nega+=f[i][u]
		if (1<=abs(f[i][u])<=1.5):
			multiply*=f[i][u]**2
	b3.append("b"+str(i+1)+"="+str(nega))
	b4.append("b"+str(i+1)+"="+str(multiply))
print("Наибольшие из значений элементов k-й строки:", *b1)
print("Cумма наибольшего и наименьшего из значений элементов k-й строки:",*b2)
print("Число отрицательных элементов в k-й строке:",*b3)
print("Произв. кв. тех эл. k-й стр., модули которых прин. отр. [1, ..., 1.5]:",*b4)