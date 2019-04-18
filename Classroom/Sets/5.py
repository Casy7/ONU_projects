'''6. Даны два списка чисел, которые могут содержать до 10000 чисел каждый. 
Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.'''
from random import randint
lenth=int(input("Введите длину списков: "))
def cr_rand_tup(min=0,max=10,len=10):
	tup=[]
	for i in range(len):
		tup.append(randint(min,max))
	tup=tuple(tup)
	return(tup)
first_set=set(cr_rand_tup(0,1000,lenth))
second_set=set(cr_rand_tup(0,1000,lenth))
counter=first_set.intersection(second_set)
print("Общие:", sorted(counter))