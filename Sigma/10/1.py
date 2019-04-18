class Person():
    def __init__ (self,fst_name,srd_name,more_info={}):
        self.fst_name = fst_name
        self.srd_name = srd_name
        self.more_info = more_info
class Book():
    def __init__ (self,name,mobile_phone,work_phone="",second_phone="",mail="",more_info={}):
        self.name = name
        self.second_phone = second_phone
        self.more_info = more_info
        self.work_phone = work_phone
        self.mail = mail
    def info(self):
        print(self.name,self.mail)
        for i in self.more_info:
            print(i,": ",self.more_info[i],sep="")
    def add_second_mail(self,input_mail):
        self.second_mail = input_mail
    def add_else_info(self,kind_of_info,info):
        self.more_info[kind_of_info] = info



pirr = Book(name = "Pirr",mobile_phone = "3141592653",mail="epbitkplz@gmail.com")#,"299792458","2718281828","epbitkplz@gmail.com")
pirr.add_else_info("Должность","Младший дворник")
pirr.info()
