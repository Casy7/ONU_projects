def crypto(text="Чики-брики в дамке",mv=3):
    
    text2=""
    for i in range(len(text)):
        text2+=chr(ord(text[i])+mv)
    #r = list(text2.encode("UTF-8"))  #переводит байт-код в список

    r = text2.encode("utf-16")  #просто переводит в байт-код
    #print(text2)

    #print(r)
    r=r[::-1]
    #print(r)

    text3 = r.decode("utf-16")
    #print(text3)
    return text3

def decrypto(text3 = "㠄㴄㼄㌄㜄⌀㔄⌀㬄㴄㬄䌄㐄　㬄㴄㬄⨄￾",mv=3):
    r=text3.encode("utf-16")
    r=r[::-1]
    text2 = r.decode("utf-16")

    #print(r)
    #print(text2)

    text=""
    mv=3
    for i in range(len(text2)-1):
        text+=chr(ord(text2[i])-mv)

    #print(text)
    return text

print(decrypto(crypto("Ho-ho-ho-хо-хор")))



