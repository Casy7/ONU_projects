'''
Проверьте, является ли данный массив возрастающим или убывающим.
'''
#a=[1,1,1,1,1,1,1,1,1,1]
#a=[35432,456,54,4,-6,-457.45]
#a=[1,52,3,443,5,6342,7,8]
a=[1,4,16,64]
up=True
down=True
for i in range(len(a)-1):
	if a[i]>=a[i+1]:
		up=False
	if a[i]<=a[i+1]:
		down=False 
	if up==False and down==False:
		break 
if(up == True):
    print("Массив сортирован по возрастанию")
elif(down == True):
    print("Массив сортирован по убыванию")
else:
    print("Массив не сортирован по возрастанию или убыванию")