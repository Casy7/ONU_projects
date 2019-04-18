'''2. Создать первый кортеж из 10 случайных чисел 
(от 1 до 10) и второй — из удвоенных элементов первого ( использовать генератор списков) '''
from random import randint
def cr_rand_tup(min=1,max=10):
	tup=[]
	for i in range(10):
		tup.append(randint(min,max))
	tup=tuple(tup)
	return(tup)
first_tuple=cr_rand_tup()
second_tuple=tuple([first_tuple[i]*2 for i in range(len(first_tuple))])
print(first_tuple,"\n",second_tuple)