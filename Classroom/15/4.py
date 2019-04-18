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
				m1.append(randint(0,r))
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
b5=[]
for i in range(m):
	b1.append(sum(f[i]))
	b3.append(min(f[i]))
	b5.append(max(f[i])-min(f[i]))
	multiply=1
	aver=0
	for u in range(n):
		multiply*=f[i][u]
		aver+=f[i][u]
	b2.append(multiply)
	if (aver/n)%1==0:
		aver=int(aver/n)
	else:
		aver=round(aver/n,1)
	b4.append(aver)
print("Суммы элементов строк:", *b1)
print("Произведения элементов строк:",*b2)
print("Наименьшие значения элементов строк:",*b3)
print("Значения средних арефметических элементов строк:",*b4)
print("Разности наибольших и наименьших значений элементов строк:",*b5)