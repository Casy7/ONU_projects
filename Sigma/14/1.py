class Person:

    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)


class Emploee(Person):

    def __init__(self, name, age, company):
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.__company = company

    def display_info(self):
        super().display_info()
        print("Company:", self.__company)
        # print("Имя:", self.name, "\tВозраст:", self.age,
        # "\nCompany:",self.__company)

tonyStark = Person("Thony Stark", 45)

# print(tonyStark.age)

tonyStark.display_info()
blackWindow = Emploee("Natash Rostova", 25, "Apple")

# print(blackWindow.age)

blackWindow.display_info()
