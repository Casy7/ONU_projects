class Person(object):
    def __init__(self, name,
                 mobile_phone=None, office_phone=None,
                 private_phone=None, email=None):
        self.name = name
        self.mobile = mobile_phone
        self.office = office_phone
        self.private = private_phone
        self.email = email

    def add_mobile_phone(self, number):
        self.mobile = number

    def add_office_phone(self, number):
        self.office = number

    def add_private_phone(self, number):
        self.private = number

    def add_email(self, address):
        self.email = address

    def __str__(self):
        s = self.name + '\n'
        if self.mobile is not None:
            s += 'mobile phone:   %s\n' % self.mobile
        if self.office is not None:
            s += 'office phone:   %s\n' % self.office
        if self.private is not None:
            s += 'private phone:  %s\n' % self.private
        if self.email is not None:
            s += 'email address:  %s\n' % self.email
        return s

class PhoneBook(object):
    def __init__(self,contacts = None):
        if contacts != None:
            self.contacts = {x.name: x for x in contacts}
        else:
            self.contacts = {} 
        # dict of Person instances
        #def __init (self, person)
    def add(self, name=None, mobile=None, office=None,
            private=None, email=None, person = None):
        if person != None:
            self.contacts[person.name] = person
        elif name != None:
            p = Person(name, mobile, office, private, email)
            self.contacts[name] = p

    def __call__(self, name):
        return self.contacts[name]

    def __str__(self):
        s = ''
        for p in sorted(self.contacts):
            s += str(self.contacts[p]) + '\n'
        return s
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