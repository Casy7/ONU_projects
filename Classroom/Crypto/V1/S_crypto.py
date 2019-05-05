
text = "Чики-брики в дамке"
mv=3
text2=""

for i in range(len(text)):
    text2+=chr(ord(text[i])+mv)
#r = list(text2.encode("UTF-8"))  #переводит байт-код в список

r = text2.encode("utf-16")  #просто переводит в байт-код

print(text2)

print(r)
r=r[::-1]
print(r)

text3 = r.decode("utf-16")
#text3 = "".join(map(chr, r))  #Пока что помойка

print(text3)






