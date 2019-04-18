s=input("Введите строку:   ")
gl=['a','e','y','u','i','o','у','е','ы','а','о','э','я','и','ю']
i=0
while len(s)>i:
 if s[i]in gl:
  s=s[0:i]+s[i+1:]
 else:
  i+=1
print(s)