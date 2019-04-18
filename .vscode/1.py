word_string = "aaaaabbbbcccdde"
word_freq ={}
for i in range(len(word_string)):
	if word_freq[word_string[i]]==None:
		word_freq[word_string[i]]=0
	word_freq[word_string[i]] +=1
	word_string=word_string[1:]
print(word_freq)
