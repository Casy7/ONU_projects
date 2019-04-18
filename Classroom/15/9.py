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
g=create(8)
printarray(g)
t=0
g1=g[:]
for i in range(8):
	for j in range(8):
		g1[i][j]=abs(g1[i][j])
sums=g1[0]
for i in range(8):
	for j in range(7):
		sums[i]+=g1[j+1][i]
ind=sums.index(max(sums))
r=[]
for i in range(8):
	r.append(g[i][ind])
print("Результат:", min(r))
