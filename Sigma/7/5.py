class Product(object):
	def __init__(self, product, price):
		self.product = product
		self.price = price
  
class ShoppingCart(object):
	items_in_cart = {}
	def __init__(self, customer_name):
		self.customer_name = customer_name

	def add_item(self, instance):
		"""Добавляет продукт в корзину."""

		if not instance.product in self.items_in_cart:
			self.items_in_cart[instance.product] = instance.price
			print(instance.product + " добавлен.")
		else:
			print(instance.product + " уже в корзине.")

	def remove_item(self, instance):
		"""Удаляет продукт из корзиные."""
		if instance.product in self.items_in_cart:
			del self.items_in_cart[instance.product]
			print(instance.product + " убран.")
		else:
			print(instance.product + " нет в корзине.")

	def total_sum(self):
		"""Суммирует цены всех элементов."""
		return sum(self.items_in_cart.values())

	def clear(self):
		"""Очищает корзину покупателя."""
		self.items_in_cart = {}

my_cart = ShoppingCart('Vadym')

product1 = Product('TV', 1000)
product2 = Product('Xbox', 5000)

my_cart.add_item(product1)
my_cart.add_item(product2)
#my_cart.remove_item(product2)
#print(my_cart.items_in_cart)
sum = my_cart.total_sum()
print(sum) #2000
my_cart.clear()
#print(my_cart.items_in_cart)