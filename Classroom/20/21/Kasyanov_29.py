'''29. Ввести два отсортированных массива. Написать
программу слияния эти массивов так, чтобы новый
массив оказался отсортированным.'''
print ( "Введите элементы первого списка:" )
a = list( map(float, input().split()))
for i in range(len(a)):
	if(a[i]%1==0):
		a[i]=int(a[i])
print ( "Введите элементы второго списка:" )
B = list( map(float, input().split()))
for ty in B:
	b=B[0]
	if(len(a)==1):
		if(b<=a[0]):
			if(b%1==0):
				b=int(b)
			a=[b]+a
		else:
			if(b%1==0):
				b=int(b)
			a=a+[b]
	else:
		L=0
		R=len(a)-1
		for j in range(len(a)//2+1):
			if((L+R)/2%1==0):
				i=int((L+R)/2)
			else:
				i=int((L+R)/2+1)
			if(a[i-1]<=b<=a[i]):
				if(b%1==0):
					b=int(b)
				a=a[0:i]+[b]+a[i:]
				break
			elif(b>=a[len(a)-1]):
				if(b%1==0):
					b=int(b)			
				a=a+[b]
				break
			elif(b<=a[0]):
				if(b%1==0):
					b=int(b)
				a=[b]+a
				break
			elif(b<a[i]):
				R=i
			else:
				L=i
	B=B[1:]
print(a)
	