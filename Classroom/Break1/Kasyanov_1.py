'''
1.Есть ли среди цифр числа четные ?
'''
a=input("Введите число:  ")
i=0
f=False
while (len(a)>0):
	if(int(a[0])%2==0):
		f=True
		break
	a=a[1:]
	i+=1
if(f==True):
	print("Чётные цифры есть")
else:
	print("Чётных цифр нет")
