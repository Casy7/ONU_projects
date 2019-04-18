F1="A"
F2="B"
lenth=int(input())
string=input()				
finstr=""
if(lenth==1 and string=="B"):
	e=0
else:																
	for i in range(lenth):
		F3=finstr				
		finstr+=F2+F1
		F1=F2		
		F2=F3
	#print(finstr)
	e=finstr.count(string)
print(e)
