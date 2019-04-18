'''3. Заполнить массив N*M случайными целыми числами и найти сумму элементов главной
диагонали получившейся матрицы'''
from random import randint
m=int(input("Введите длину массива:  "))
n=int(input("Введите ширину массива:  "))
def t(c):
	for i in range(len(c)):
		print(*c[i])

g=[]
for i in range(m):
	m1=[]
	for j in range(n):
		m1.append(randint(0,9))
	g.append(m1)
t(g)