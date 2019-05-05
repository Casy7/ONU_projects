text = "У лукоморья дуб квадратный"
mv=3
text2=""
for i in range(len(text)):
    text2+=chr(ord(text[i])+mv)
r = text2.encode("UTF-8")
print(r.decode("UTF-8"))
print(text2)