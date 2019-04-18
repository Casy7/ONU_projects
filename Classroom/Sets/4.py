'''4. Дан список чисел, который могут 
содержать до 100000 чисел каждый. Определите, сколько в нем встречается различных чисел.'''
from random import randint
lenth=int(input("Введите длину списка: "))
def cr_rand_tup(min=0,max=10,len=10):
	tup=[]
	for i in range(len):
		tup.append(randint(min,max))
	tup=tuple(tup)
	return(tup)
first_tuple=cr_rand_tup(0,5,lenth)

counter=[]
for i in range(lenth):
	if first_tuple[i] not in counter:
		counter.append(first_tuple[i])
print("Различных:", len(counter))