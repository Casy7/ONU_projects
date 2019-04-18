a="Claess3Scrholar1 Class3Scholar2, Class3Scholar3, Class3Scholar4 Class3Scholar 5, Scholar6, Scholar7, Class2Scholar1, Class2Scholar2, Class4Scholar3"
a_inp="Class3 Class2"
a=a.lower()
result=[]
i=0
p=0
aa1="Class Scholar "
while len(a)>0:
	arr=['']*2
	a1=list(a[:18])
	while(i<len(a1)):
		if(a[i] in a1):
			p+=1
		if(a[i] == a1[i]):
			i+=2
	if i>10:
		a3=a1
		for i in range(len(a1)):
			if(a1[0].isdigit()):
				arr[0]=a1[0]
				a1=a1[1:]
				break
			else:
				a1=a1[1:]
		for i in range(len(a1)):
			if(a1[0].isdigit()):
				arr[1]=a1[0]
				a1=a1[1:]
				break
			else:
				a1=a1[1:]
	else:
		print("Ошибка ввода")
	sp=a.find(" ")
	co=a.find(",")
	
	if sp<co:
		a=a[sp:]
	elif sp>co:
		a=a[co:]
	else:
		a[16:]
	a=a.strip(" ").strip(",").strip(" ")
	sd=["Class"+arr[0],"Schoolar"+arr[1]]
	if(["Class"+arr[0]] in result)==False:
		result.append(sd)
	else:
		r=result.index(arr[0])
		result[r].append([sd])	
	if(sp==co and sp==-1):
		break	
	fi=0
	for fi in range(len(a)-2):
		if(a[fi]=="c" and a[fi+1]=="l" and a[fi+2]=="a"): 
			a=a[fi:]
			break

final=["",""]*10
for u in range(len(final)):
	if u%2==1:
		final[u]=list(final[u])
result.sort()
i=0
while i<len(result)+20:
	final[i]=result[0][0]
	if len(result)<2:
		final[i+1]+=[result[0][1]]
		break
	while  final[i]==result[0][0]:
		final[i+1]+=[result[0][1]]
		result.remove(result[0])
	i+=2
r=len(final)-1
while(r>1):
	if(final[r]=="" or final[r]==[]):
		final.remove(final[r])
	r-=1
qw=a_inp.split(" ")
out=[]
for i in range(len(qw)):
	out+=[qw[i]]
	out+=[final[final.index(qw[i])+1]]
print(out)
