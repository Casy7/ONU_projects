class Computer():
	def __init__(self, keyboard, monitor, power_supply, drive, model = None,condit = "Off",os = None,version = None):
		self.keyboard = keyboard
		self.monitor = monitor
		self.power_supply = power_supply
		self.drive = drive
		self.model = model
	def turn_on (self):
		self.condit = "On"

	def turn_off (self):
		self.condit = "Off"

	def printout(self):
		print("Hello world")

	def instal_system(self, current_system):
		self.system = current_system

	def upgrade(self,up_version_to):
		self.version = up_version_to

class Desktop (Computer):
	def __init__(self, keyboard, monitor, power_supply, drive, model = None, secondary_monitors = [], condit = "Off",os = None,version = None):
		self.power_supply = power_supply
		self.drive = drive
		self.secondary_monitors = secondary_monitors
		self.model = model
	def mon_add(self,monitor):
		self.secondary_monitors.append(monitor)

class Laptop (Computer):
	def __init__(self, keyboard, monitor, power_supply,  drive, model, battery = 100,close_condition = "Close", condit = "Off",os = None,version = None):
		self.battery = battery
		self.drive = drive
		self.close_condition = close_condition
		self.model = model
	def check_closed (self):
		if self.close_condition == "Close" and self.condit == "On":
			self.turn_off()
		elif self.close_condition == "Open" and self.condit == "Off":
			self.turn_on()

	def check_battery(self):
		print(self.battery)
		if self.battery<=15:
			print("Low charge:", self.battery)

class MacBook (Laptop):
	def __init__(self, drive, model,keyboard="standart",  battery=100, close_condition = "Close", condit = "Off",os = "MacOS",version = "2.3"):
		#self.monitor = monitor
		#self.power_supply = power_supply
		self.drive = drive
		self.close_condition = close_condition
		self.model = model
	def EFI(self):
		print("EFI Boot")

top_desktop = Desktop(keyboard = "Corsair Platinum", monitor = "Samsung", power_supply = "Asus ROG",drive = "DDR4",secondary_monitors=["Samsung"],os="Windows",version=10.5)
linux_laptop = Laptop(model = "Acer 100 500",keyboard = "Some_keyb", monitor = "monit", power_supply = "integrated",drive = "DDR4",os="Linux")
some_macbook_pro = MacBook (model = "MacBook pro", drive = "DDR4",battery=15,os = "Ubuntu")
top_desktop.turn_on()
linux_laptop.turn_on()
some_macbook_pro.turn_on()	

#some_macbook_pro.EFI()
#some_macbook_pro.check_battery()

print(top_desktop.model)
print(linux_laptop.model)
print(some_macbook_pro.model)