'''Получить [aij] i = 1, ..., 10; j = 1, ..., 12 - целочисленную матрицу, для которой
aij = i + 2j.'''
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
b=create(10,13)
b[0]=[i for i in range(13)]
for i in range(1,len(b)):
	b[i][0]=i	
	for j in range(1,len(b)+1):
		b[i][j]=i+2*j
printarray(b)