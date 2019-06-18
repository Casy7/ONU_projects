
text3 = "㠄㴄㼄㌄㜄⌀㔄⌀㬄㴄㬄䌄㐄　㬄㴄㬄⨄￾"
r=text3.encode("utf-16")
r=r[::-1]
text2 = r.decode("utf-16")



print(r)
print(text2)

text=""
mv=3
for i in range(len(text2)-1):
    text+=chr(ord(text2[i])-mv)

print(text)