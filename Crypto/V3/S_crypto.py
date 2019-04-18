def crypto(text="Чики-брики в дамке",mv=3):
    
    text2=""
    for i in range(len(text)):
        text2+=chr(ord(text[i])+mv)
    #r = list(text2.encode("UTF-8"))  #переводит байт-код в список

    r = text2.encode("utf-8")  #просто переводит в байт-код
    #print(text2)

    #print(r)
    #
    #print(r)

    #text3 = r.decode("utf-16")
    #print(text3)
    #return text3
    r2=""
    r2+=str(repr(r))[2:-1]    
    print(r2)
    r2 = r2.replace("\\x","g")

    r2=r2[::-1]

    return r2



print(crypto())
