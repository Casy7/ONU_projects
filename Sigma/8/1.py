class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model
Car.wheels=8
mustang = Car('Ford', 'Mustang')
lamborgini = Car('Ferrari', 'F50')
print (mustang.wheels)
print (lamborgini.wheels)
