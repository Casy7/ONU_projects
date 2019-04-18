from random import randint
a=[]
b=[]
for i in range(5000):
	a.append("TestUser["+str(randint(1,1000))+"]")
	b.append("AnotherTestUser["+str(randint(1,1000))+"]")
c=a+b	
c.sort()
print(c)