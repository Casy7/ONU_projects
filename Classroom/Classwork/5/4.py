from random import randint
m=int(input("Разрядность:  "))
def t(c):
	for i in range(len(c)):
		print(*c[i])
g=[]
for i in range(m):
	m1=[]
	for j in range(m):
		m1.append(randint(0,9))
	g.append(m1)
print("Матрица:")
t(g)
print("Результат:")
for j in range(m):
	g[j][m-1],g[m-1][j]=g[m-1][j],g[j][m-1]
for j in range(m-1):
	g[j][0],g[0][j]=g[0][j],g[j][0]
t(g)
