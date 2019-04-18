'''Найдите наименьший четный элемент массива.'''
a=input("Введите массив чисел(через запятую):  ")
a=a.replace(" ","")
a=a.split(",")
co=0
g=len(a)
for i in range(g):
	a[i]=float(a[i])
for i in range(g):		
	if i%2!=0:
		a[i]="-="
i=0
while("-=" in a):		
	if a[i]=="-=":
		a.remove(a[i])
	i+=1
for i in range(len(a)):
	a[i]=float(a[i])
res=min(a)
print(res)