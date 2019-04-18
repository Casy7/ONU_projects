'''
Дан произвольный текст. Найдите номер первого самого длинного слова в нем.
'''
le=[]
a="Мой дядя самых честных правил,"
a=a.split()
for u in range(len(a)):
	le.append(len(a[u]))
for u in range(len(a)):
	if max(le)==len(a[u]):
		print(u+1)
		break
	