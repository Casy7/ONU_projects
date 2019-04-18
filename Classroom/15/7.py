'''В данной действительной матрице размера 6 x 9 поменять местами строку,
содержащую элемент с наибольшим значением, со строкой, содержащий
элемент с наименьшим значением. Предполагается, что эти элементы
единственны.'''
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
#n=int(input("Введите порядок матрицы: "))
g=create(6,9,r=20)
printarray(g)
print("")
b1=[]
b2=[]
for i in range(6):
	b1.append(min(g[i]))
	b2.append(max(g[i]))
g[b1.index(min(b1))],g[b2.index(max(b2))]=g[b2.index(max(b2))], g[b1.index(min(b1))]
printarray(g)
