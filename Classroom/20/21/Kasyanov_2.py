'''1. Написать программу сортировки списка по убыванию методом пузырькa'''
print ( "Введите элементы массива:" )
A = list( map(float, input().split()) )
N = len(A)
for i in range(N-1):
	for j in range(N-i-1):
		if A[j] < A[j+1]:
			A[j+1],A[j] = A[j],A[j+1]
print ( "Отсортированный список: " )
for x in A:
	print ( x, " ", end="", sep="" )
d=0
for x in range(len(A)-1):
	if(A[x]==A[x+1]):
		d+=1
print ( "\nРазличных элементов: ",len(A)-d) 