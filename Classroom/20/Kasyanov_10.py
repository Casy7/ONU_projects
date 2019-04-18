'''Даны две дроби a/b и c/d(числа a и c — целые, b и d — натуральные). Вычислите их
сумму и запишите ее в виде смешанной дроби x y/z(число xцелое, числа y z целое
натуральные, дробь y/z— правильная несократимая)'''
a1=input("Введите числа a,b,c,d(через запятую):  ")
a1=a1.replace(" ","")
a1=a1.split(",")
a=int(a1[0])
b=int(a1[1])
c=int(a1[2])
d=int(a1[3])
num=a*d+b*c
minus=""
if(num<0):
	minus="-"
	num=-num
den=b*d
whole=0
while num>den:
	whole+=1
	num-=den
	
den1=den
num1=num
gcd=1
while den1!=0 and num1!=0:
	if den1>num1:
		den1%=num1
	else:
		num1%=den1
	gcd=den1+num1
den/=gcd
num/=gcd
den=int(den)
num=int(num)
if(whole==0):
	whole=""
if num==0:
	print("0")
elif (num/den)%1==0:
	print(int(float(minus+str(whole+num/den))))
else:
	print(minus+str(whole)+" "+str(num)+"/"+str(den))