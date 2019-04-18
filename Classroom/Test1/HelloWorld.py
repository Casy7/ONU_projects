'''
2. Выбрать числа из строки
'''
S="809Du5467bdrub7997867"
a=""
print(S)
while (len(S)>0):
	q=S[0]
	if(q.isalpha==True):	
		S=S[1:]
		print(S)
	else:		
		t=0
		w=""
		print("xtjty")
		while(q.isalpha==False):
			w=w+S[t]
			t+=1
			S=S[1:]			
		a=a+", "+w

		
print(a)