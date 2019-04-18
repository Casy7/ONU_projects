'''
6.Написать программу-тест числа на простоту
'''
n=int(input("Введите число:   "))
i=2
f=False
while (i<=n**0.5):
	if n%i == 0:
		f = True
		break
	i+=1
if (f==True):
	print ("Число не простое")
else:
	print ("Число простое")