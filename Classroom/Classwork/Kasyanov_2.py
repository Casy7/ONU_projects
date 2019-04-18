'''
2. Выбрать числа из строки
'''
S=input("Введите строку:   ")
a=[]

while (len(S)>0):
	if (S[0].isdigit()):
		t=0
		w=""
		while(len(S)>0 and S[0].isdigit()):
			w=w+S[t]
			S=S[1:]
		a=a+[w]	
	S=S[1:]
print(a)