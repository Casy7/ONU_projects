'''
5.Даны две действительные квадратные матрицы порядка n. Получить новую
матрицу умножением элементов каждой строки первой матрицы на наибольшее
из значений элементов соответствующей строки второй матрицы;
'''
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
	for i in range(m):
		g[j][i]="{:5g}".format(g[j][i]*max(h[j]))
t(g)
