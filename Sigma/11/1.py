class Vehicle(object):
    base_sale_price = 0

    def __init__(self, wheels, miles, sold_on=None, 
    make=None, model=None, year=None):
        """Return a new Truck object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this truck as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the truck."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)


truck = Vehicle(6, 60000, 2024, "Tesla", "xxxl", 2022)
print(truck.sale_price())
print(truck.purchase_price())


class Car(Vehicle):

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Car object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.base_sale_price = 8000


class Truck(Vehicle):

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Truck object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.base_sale_price = 10000


some_truck = Truck(6, 6000, 2040, "Lada", "new", 2042)
some_car = Truck(4, 1000, 2019, "GermInd", "newest", 2019)
print(some_car.model)
print(some_truck.model)
print(some_car.sale_price())
print(some_truck.purchase_price())
