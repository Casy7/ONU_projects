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
n=int(input("Введите порядок матрицы: "))
g=create(n,n,r=20)
printarray(g)
b1=[]
for i in range(n):
	b1.append(min(g[i]))
print(sum(g[b1.index(min(b1))]))

