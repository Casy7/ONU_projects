
class Fruit(object):
    """Класс, который готовит очень вкусные фрукты."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print("Я %s %s и я на вкус %s." % (self.color, self.name, self.flavor))

    def is_edible(self):
        if not self.poisonous:
            print("Не ешь меня! Я съедобный.")
        else:
            print("Ага! Я супер отравленный.")


# Инициализация объекта lemon
lemon = Fruit("лимон", "желтый", "кислый", False)

# Вызов метода description()
lemon.description()

# Вызов метода is_edible()
lemon.is_edible()