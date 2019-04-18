F=["","A","B",""]
lenth=int(input())
string=input()				
finstr=""																
for i in range(0,lenth):
	F[3]=finstr				
	if(F[0]==''):
		finstr+=F[1]+F[0]
		F[0]='0'
		continue
	else:
		finstr+=F[2]+F[1]
	F[0]=F[1]	
	F[1]=F[2]
print(finstr)
e=finstr.count(string)
print(e)