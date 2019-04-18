'''Заданы день и месяц рождения, а также текущие день, месяц и год. Определить,
сколько дней осталось до дня рождения.'''
ddmm=input().split(" ")
dmy=input().split(" ")
for i in range(2):ddmm[i]=int(ddmm[i])
for i in range(3):dmy[i]=int(dmy[i])    
m=[31,28]
for i in range(10):
	if(i%2):
		m.append(30)
	else:
		m.append(31)
mv=[m[0],29]+m[2:]
if(dmy[0]%400==0 or (dmy[0]%4==0 and dmy[0]%100!=0)):
	m=mv
i=0
days=0
while(ddmm[0]<dmy[0] or ddmm[1]<dmy[1]):
	if(ddmm[0]>m[i]):
		ddmm[0]=0
		ddmm[1]+=1
		i+=1	
	ddmm[0]+=1
	days+=1
print(days)