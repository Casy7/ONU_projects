'''from Person import Person
from PhoneBook import PhoneBook
'''

from Person import Person
from Phon import PhoneBook
mike = Person("Mike Janes", "21312312", office_phone="232131")
jhon = Person("Jhon Snow", "13424343", office_phone="22323")

myPhoneBook = PhoneBook()

myPhoneBook.add('Ole Olsen', office='767828292',
      email='olsen@somemail.net')

myPhoneBook.add('Hans Hanson',
      office='767828283', mobile='995320221')

myPhoneBook.add('Per Person', mobile='906849781')

myPhoneBook.add(person=mike)
myPhoneBook.add(person=jhon)

print(myPhoneBook)

alen = Person("Alen Page", "2321312", office_phone="22323", private_phone="213123444")
contacts = [mike, jhon, alen]
myPhoneBook2 = PhoneBook(contacts=contacts)

print(myPhoneBook2)