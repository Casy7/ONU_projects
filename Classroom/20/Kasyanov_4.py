'''
Найдите сумму нечетных чисел списка, которые не превосходят 11.
'''
a=input().split(" ")
count=0
for i in range(0,len(a),1):
    a[i]=int(a[i])
    if a[i]%2==1 and a[i]<11:
        count+=a[i]
print(count)