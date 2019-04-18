min_orders = 5
min_price = 20
customers = {
'Петя' : [22, 30, 11, 17, 15, 52, 27, 12], # Только 4 заказа на сумму 20$ или больше, никакой бесплатной пиццы
'Маша' : [5, 17, 30, 33, 40, 22, 26, 10, 11, 45],
'Сигизмунд' : [5, 17, 30, 33, 40, 22, 26, 10, 11, 45] # Есть 6 заказов на сумму 20$ или больше, а это значит - Пицца на шару!
}

def pizza_rewards(customers=[], min_orders=5, min_price=20):
	eligible=[]
	names_customers=list(customers.keys())
	for i in range(len(customers)):
		list_of_purchases=customers[names_customers[i]]
		counter=0
		for j in range(len(list_of_purchases)):
			if(list_of_purchases[j]>=min_price):
				counter+=1
		if counter>=min_orders:
			eligible.append(names_customers[i])
	return eligible
print(pizza_rewards(customers))