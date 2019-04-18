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
f=create(6,9,99)
printarray(f)
b1=[]
b2=[]
for i in range(6):
	b1.append(min(f[i]))
	b2.append(max(f[i]))
print("Результат:",min(b1)+max(b2)/2)
