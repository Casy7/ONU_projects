'''
Проверьте, образует ли элементы массива в данном порядке арифметическую или
геометрическую прогрессии.
'''
#a=[1,2,3,4,5,6,7,8]
a=[1,4,16,64]
ar=a[1]-a[0]
geo=a[1]/a[0]
arb=True
geob=True
b=True
for i in range(len(a)-1):
    if a[i]!=a[i+1]-ar:
      arb=False
    if a[i]!=a[i+1]/geo:
      geob=False  
    if arb==False and geob==False:
        break
    if ar==0 or geo ==0:
        geob=False 
        arb=False
if(arb == True):
    print("Элементы образуют арифметическую прогрессию")
elif(geob == True):
    print("Элементы образуют геометрическую прогрессию")
else:
    print("Элементы не образуют прогрессию")