word_string = "aaaaabbbbcccdde"
word_freq = {}
for i in range(len(word_string)):
	word_freq[word_string[i]] = 1
for i in range(len(word_string)):
	while len(word_string)>1 and word_string[0]==word_string[1]:
		word_freq[word_string[0]] += 1
		word_string=word_string[1:]
	word_string=word_string[1:]
print(word_freq)