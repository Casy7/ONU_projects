class CashMachine():
    # 1
    def __init__(
                self, bankName, balance, clients=[],
                admin=None, transfers=[]):

        self.__bankName = bankName
        self.__balance = balance
        self.__clients = clients
        # 2, 4
        self.__admin = admin
        self.__transfers = transfers

    # 3
    def setBankName(self, new_name):
        if "bank" in new_name.lower():
            self.__bankName = new_name
        else:
            print("Wrong name for Bank")

    def getBankName(self):
        return(self.__bankName)
    bankName = property(getBankName, setBankName)
    # 5

    @property
    def clients(self):
        str_to_out = "Clients of bank MonoBank are: "+str(self.__clients)
        return (str_to_out)

    # 6
    def withdraw(self, how_much, person):
        if person in self.__clients:
            if self.__balance >= how_much:
                self.__transfers.append({person: -how_much})
                self.__balance -= how_much
                print("Success withdraw of", how_much)
            else:
                print("Not enought money. Look for another cashmachine")
        else:
            print("John Snow is not client of bank")

    # 7
    @property
    def lastTransactions(self):
        if len(self.__transfers) >= 5:
            return self.__transfers[:-5:-1]
        else:
            return self.__transfers[:len(self.__transfers)]

    def uploadBalance(self, how_much, person):
        if person in self.__clients:
            self.__transfers.append({person: how_much})
            self.__balance += how_much
            print("Successfully uploading")
        else:
            print("You have no permission to upload money to cashmachine")

# 8
    @property
    def setBalance(self, balance, user):
        if user == "Admin":
            self.__balance = balance
        else:
            print("Only admins can change balance.")

    def getBalance(self):
        return self.__balance
    balance = property(getBalance, setBalance)


clients = ["Vadym", "Stas"]

privat = CashMachine("PrivatBank", 10000, clients)

privat.bankName = "Potato"  # Wrong name for Bank
print(privat.bankName)  # PrivatBank
privat.bankName = "MonoBank"
print(privat.bankName)  # MonoBank

print(privat.clients)  # Clients of bank MonoBank are: ['Vadym', 'Stas']

privat.withdraw(500, "Vadym")  # Sucess withdraw of 500
privat.withdraw(8000, "John Snow")  # John Snow is not client of bank
# Not enought money. Look for another cashmachine
privat.withdraw(100000, "Vadym")
print(privat.lastTransactions)  # [{'Vadym': 500}]


# You have no permission to upload money to cashmachine
privat.uploadBalance(5000, "John Snow")
privat.uploadBalance(5000, "Elon Musk")

print(privat.balance)  # 14500
