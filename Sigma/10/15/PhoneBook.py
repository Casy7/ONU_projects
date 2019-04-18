from Person import Person
    

class PhoneBook(object):
    def __init__(self,contacts = None,person = None):
        self.person = person
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