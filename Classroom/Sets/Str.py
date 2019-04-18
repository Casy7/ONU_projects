import pyperclip
print ('Скопируйте фрагмент файла в буфер обмена.')
fragment=input("Введите букву/фрагмент: ")
line=pyperclip.paste()
#print(line)
lenth_line=len(line)
counter=line.count(fragment)
rate=len(fragment)*counter/lenth_line
if len(fragment)==1:
	type_of_fragment="буквы"
else:
	type_of_fragment="фрагмента"
print ("Количество повторений ",type_of_fragment," =", counter,sep='')
print ("Частота встречаемости ",type_of_fragment," =", round(rate,7),sep='')