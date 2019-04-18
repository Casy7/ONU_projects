n = int(input())
m=input().split()
c=0
for i in m:
	if float(i)<30:
		c+=1
mk=(c*0.2)/0.9
if(not round(mk,5)%1==0):
	mk=int(mk+1)
print(mk,c)