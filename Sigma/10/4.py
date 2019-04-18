class Person():
    def __init__ (self, name,last_name, mobile_phone="", work_phone="",second_phone="",mail="",more_info={}):
        self.name = name
        self
        self.second_phone = second_phone
        self.more_info = more_info
        self.work_phone = work_phone
        self.mail = mail
    #self.name = Person(name)

    def info(some_pers):
        #print(some_pers.name)#,some_pers.mail)
        info_to_output = list(some_pers.__dict__)
        dict_to_out = some_pers.__dict__
        #print(info_to_output)
        for i in info_to_output:
            if i!="more_info":
                print(i.center(26),dict_to_out[i].center(26))
        for i in some_pers.more_info:
            print(i,": ",some_pers.more_info[i],sep="")

    def add_adress(self, adress):
        self.adress = adress
    def add_mail(self,input_mail):
        self.mail = input_mail
    def add_work_phone(self,input_work_phone):
        self.work_phone = input_work_phone
    def add_second_phone(self,input_second_phone):
        self.second_phone = input_second_phone

    def add_else_info(self,kind_of_info,info):
        self.more_info[kind_of_info] = info
    #def print_short(some_pers):

class Phone_Book():
    def __init__ (self, name, last_name):
        self.name = name
        self.last_name = last_name

    def sort_contacts(self):
        list_of_names = []
        for i in range(len(list_of_contacts)):
            list_of_names.append(list_of_contacts[i].name)
        list_of_names.sort()
        print(list_of_names)
    

pirr = Person("Pirr", "Holy","3141592653","299792458","2718281828","epbitkplz@gmail.com")
john = Person("John","Johmson")
smidt = Person("Smidt","Smidtson")
list_of_contacts = [pirr,smidt, john]
pirr.add_else_info("Должность","Младший дворник")
pirr.add_else_info("Власть",1000)
pirr.info()
Phone_Book.sort_contacts(Phone_Book)
