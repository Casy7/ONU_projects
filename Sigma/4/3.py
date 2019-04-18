def isAnagram(inp, inpcheck):
    inp = list(inp.lower())
    inpcheck = list(inpcheck.lower())
    boolcheck = True
    for i in range(len(inp)):
        if inpcheck[i] not in inp or \
        inp.count(inpcheck[i]) != inp.count(inpcheck[i]):
            boolcheck = False
    return(boolcheck)


str1 = "Buckethead"
str2 = "DeathCubeK"
str3 = "foefet"
str4 = "toffee"
print(isAnagram(str1, str2))
print(isAnagram(str3, str4))
