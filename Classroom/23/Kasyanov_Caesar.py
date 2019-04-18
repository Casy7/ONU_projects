#alphabet = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
def encodeCaesar(filein, fileout, key):
	with open (filein,"r") as file:
		str_of_file =""
		for line in file:
			str_of_file+=line
		str_to_out = ""
		for ch in range(len(str_of_file)):
			str_to_out+=chr(ord(str_of_file[ch]) + key)
	with open (fileout,"w",encoding = "UTF-8") as file:
		file.write(str_to_out)
	return str_to_out
def decodeCaesar(filein, fileout, key):
	with open (filein,"r") as file:
		str_of_file =""
		for line in file:
			str_of_file+=line
		str_to_out = ""
		for ch in range(len(str_of_file)):
			str_to_out+=chr(ord(str_of_file[ch]) - key)
	with open (fileout,"w",encoding = "UTF-8") as file:
		file.write(str_to_out)
	return str_to_out
print(encodeCaesar("1.txt","2.txt",5))
print(decodeCaesar("2.txt","3.txt",5))
