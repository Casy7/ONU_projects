'''
Найдите количество элементов массива, которые отличны от наибольшего элемента не более
чем на 10%.
'''
a=input("Введите массив чисел(через запятую):  ")
a=a.replace(" ","")
a=a.split(",")
co=0
for i in range(len(a)):
	a[i]=float(a[i])
maxim=max(a)
for i in range(len(a)):
	if 0.9*a[i]<=maxim<=1.1*a[i]:
		co+=1
print(co-1)
