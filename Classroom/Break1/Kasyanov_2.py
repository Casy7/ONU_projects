'''
2.Входит ли в строку хоть одна гласная буква
'''
a=input("Введите строку:  ")
i=0
f=False
a=a.lower()
while (len(a)>0):
	if(a[0]in["а","о","у","э","и","я","ю","е","и"]):
		f=True
		break
	a=a[1:]
	i+=1
if(f==True):
	print("В строке есть по крайней мере одна гласная")
else:
	print("Гласных нет")
