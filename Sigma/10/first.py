class Person():
	def __init__ (self, name, mobile=None, office_phone=None,private_phone=None,email=None,more_info=None):
		self.name = name
		self.private_phone = private_phone
		self.more_info = more_info
		self.office_phone = office_phone
		self.email = email

	def info(self,some_pers):
		info_to_output = list(some_pers.__dict__)
		dict_to_out = some_pers.__dict__
		#print(info_to_output)
		for i in info_to_output:
			if i!="more_info":
				print(i.center(26),dict_to_out[i].center(26))
		for i in some_pers.more_info:
			print(i,": ",some_pers.more_info[i],sep="")

	def add_else_info(self,kind_of_info,info):
		self.more_info[kind_of_info] = info

	def __lt__(self,persons):return self.name<persons.name

class PhoneBook():
	contacts = []
	def __init__ (self, contacts=[]):
		self.contacts = contacts
	
	def add(self, name = None,person = None,office = None, mobile = None, email = None):
			if Person==None:
				i = Person(name,mobile=mobile,office_phone=office,email=email)
				self.contacts.append(i)
			else:
				self.contacts.append(person)

	def __str__(self):
		for pers in self.contacts:
			info = pers.__dict__
			for i in info:
				if i[0]!=None:
					print(i)


mike = Person("Mike Janes", "21312312", office_phone="232131")
jhon = Person("Jhon Snow", "13424343", office_phone="22323")

myPhoneBook = PhoneBook()

myPhoneBook.add('Ole Olsen', office='767828292', email='olsen@somemail.net')
myPhoneBook.add('Hans Hanson', office='767828283', mobile='995320221')
myPhoneBook.add('Per Person', mobile='906849781')

myPhoneBook.add(person=mike)
myPhoneBook.add(person=jhon)

print(myPhoneBook)

alen = Person("Alen Page", "2321312", office_phone="22323", private_phone="213123444")
contacts = [mike, jhon, alen]
myPhoneBook2 = PhoneBook(contacts=contacts)

print(myPhoneBook2)