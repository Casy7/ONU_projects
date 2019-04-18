class Crypto():
	def __init__(self,morseFile):
		self.morseFile = morseFile

	def decode(self, encodedFile):
		with open(morseFile) as keys:
			key_list = {"":" "}
			for line in keys:
				list_line = list(line.split())   
				symbol = list_line[0][-1]
				key_list[list_line[1]] = symbol

		with open(encodedFile) as code_morse:

			input_list = []
			for line in code_morse:   
				input_list.append(line.replace("\n",""))
			output_word = []

			for line in input_list:
				output_word.append(key_list[line])
		str_to_return=""
		for i in output_word:
			str_to_return=str_to_return+i
		return str_to_return

	def encode(self,file,text):
		with open("morse.txt") as keys:
			key_list = {" ":""}
			for line in keys:
				list_line = list(line.split())   
				code_of_symbol = list_line[0][-1]
				key_list[code_of_symbol] = list_line[1]
		list_of_code=[]
		with open(file,"w") as to_decode:
			text = text.upper()
			for symbol in text:
				to_decode.write(key_list[symbol]+"\n")
				list_of_code.append(key_list[symbol])
		return(list_of_code)

morseFile = 'morse.txt'

crypto = Crypto(morseFile)

encodedFile = 'encoded.txt'
decoded = crypto.decode(encodedFile)
print(decoded)

newFile = 'newFile.txt'
message = "I am your father Luke"
morse_encode = crypto.encode(newFile, message)
print(*morse_encode, sep=' ')

decoded = crypto.decode('newFile.txt')
print(decoded)
