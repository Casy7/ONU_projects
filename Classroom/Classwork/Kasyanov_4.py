'''
4.Определить процент строчных букв в строке.
'''
S=input("Введите строку:   ")
a=0
S1=S
i=0
while (len(S)>0):
	if(S[0].isdigit()):
		i+=1
		#Где i -- счётчик цифр в строке
	if (S[0].islower()):
		a+=1	
	S=S[1:]
print(round(a/(len(S1)-i)*100,2),"%",sep="")
print()
