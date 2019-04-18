customers = {"Valya": [1, 22, 26, 45, 46, 46], "Kolya": [
    14, 13, 25], "Petya": [0, 13, 45, 45, 45, 45, 44]}


def pizza_rewards2(customers={}, min_orders=5, min_price=20):
    eligible = []
    for name in customers.keys():
        list_of_purchases = customers[name]
        orders = 0
        for purchase in list_of_purchases:
            if(purchase >= min_price):
                orders += 1
        if orders >= min_orders:
            eligible.append(name)
    return eligible


print(pizza_rewards2(customers, 5, 20))
