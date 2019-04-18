'''1.Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно. Также заполните 
второй кортеж случайными числами от -5 до 0. Для заполнения кортежей числами напишите одну функцию. 
Объедините два кортежа с помощью оператора +, создав тем самым третий кортеж. С помощью метода кортежа 
count() определите в нем количество нулей. Выведите на экран третий кортеж и количество нулей в нем. 
Определите первое и второе вхождения числа 0 в кортеж'''
from random import randint
def cr_rand_tup(min=0,max=10):
	tup=[]
	for i in range(10):
		tup.append(randint(min,max))
	tup=tuple(tup)
	return(tup)
first_tuple=cr_rand_tup(0,5)
second_tuple=cr_rand_tup(-5,0)
final_tuple=first_tuple+second_tuple
print(final_tuple)
print("Нулей:", final_tuple.count(0))
