'''6. Даны две действительные квадратные матрицы порядка n. Получить новую
матрицу прибавлением к элементам каждого столбца первой матрицы
произведения элементов соответствующих строк второй матрицы.'''
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
print("Матрица 1:")
t(g)
h=[]
for i in range(m):
	m1=[]
	for j in range(m):
		m1.append(randint(0,9))
	h.append(m1)
print("Матрица 2:")
t(h)
print("Результат:")

for j in range(m):
	u=1
	for y in range(len(h[j])):
		u*=h[j][y]
	for i in range(m):
		

		g[j][i]="{:5g}".format(g[j][i]*u)
t(g)
