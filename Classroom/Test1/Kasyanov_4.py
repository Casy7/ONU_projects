'''
4. Определить длину строки. ЕСЛИ длина строки превышает 4 символа, ТО вывести
строку в нижнем регистре.
'''
S="У лукоморья 123 дуб зеленый 456"
i=len(S)
if(i>4):
	S=S.lower()
print(S)