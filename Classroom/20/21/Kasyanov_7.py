from random import randint
print("Отгадайте число 1000<=x<10000")
a=randint(1000,9999)
i=1000
att=""
while(att!=a and i<=10000):
	att=i
	print(att)
	i+=1
print("Попыток:",i)