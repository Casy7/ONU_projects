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


class Student(Person):

    def __init__(self, name, age, university):
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.__university = university

    def display_info(self):
        # super().display_info()
        print(self.name, "\tUniversity:", self.__university)
        # print("Имя:", self.name, "\tВозраст:", self.age,
        # "\nCompany:",self.__company)


tonyStark = Person("Thony Stark", 45)
blackWindow = Student("Natash Rostova", 25, "Harward")
spiderMan = Student("Piter Parker", 18, "McDonalds")

superHeroes = [tonyStark, blackWindow, spiderMan]

for hero in superHeroes:
    hero.display_info()
