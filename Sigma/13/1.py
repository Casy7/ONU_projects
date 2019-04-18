class Computer:

    def __init__(self, cpu, powerSuply, memory, gpu=None, ssd=None):
        self.__cpu = cpu
        self.powerSuply = powerSuply
        self.memory = memory
        self.gpu = gpu
        self.ssd = ssd

    def __str__(self):
        return str(self.__dict__)

    def turnOn(self):
        return 'The computer was running'

    def turnOff(self):
        return 'The computer was off'

    def playGame(self):
        if self.gpu is not None:
            return 'Start the game'
        else:
            return 'Sorry, but you can\'t play without gpu'


class Mac(Computer):

    def __init__(self, sensitivityOfTouchpad, screen, operatingSystem=None):
        self.sensitivityOfTouchpad = sensitivityOfTouchpad
        self.screen = screen
        self.__operatingSystem = operatingSystem

    def getSystem(self):
        return self.__operatingSystem

    def setSystem(self, os):
        self.__operatingSystem = os

    def setOperatingSystemIn(self, os):
        if self.operatingSystem is not None:
            if os == "MacOs" or os == "Windows":
                self.setSystem(os)
        else:
            return 'Something isn\'t work'


linux = Computer("i9", 8000, "64GB", 8)
winTop = Computer("Pentium", 1000, "128MB", 2)
newMac = Mac("i7", "500W", "Linux")
oldMax = Mac("i3", "500W", "Linux")
# Переменные с двумя нижними подчёркиваниями нельзя менять извне
# somePc = Mac()

newMac.operatingSystem = "Ubuntu"
print(newMac.getSystem())
newMac.cpu = "i5"
newMac.setOperatingSystemIn("Windows")
print(newMac)
print(newMac.cpu)
