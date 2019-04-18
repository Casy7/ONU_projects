a=[32450,6,5,5,7,780,110,12,-13,13,19]
N = len(a)
for i in range(N-1):
	nMin = i
	for j in range(i+1,N):
		if a[j]<a[nMin]:
			nMin=j
	if i!= nMin:
		a[i],a[nMin]=a[nMin],a[i]
L=0
R=len(a)-1
b=int(input())
for j in range(len(a)):
	i=int(round((L+R)/2,0))
	if(a[i]==b):
		print(i)
		break
	if(b<a[i]):
		R=i-1
	if(L==R+1):
		print("Элемента нет")
		break
	else:
		L=i
print(a)
