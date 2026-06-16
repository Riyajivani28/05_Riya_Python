class father:
    car:int
    bal:int

    def getdata(self):
        self.car=int(input("how many car ??"))
        self.bal=int(input("how many balance in bank ??"))

class son(father):

    def printdata(self):
        print("car :",self.car)
        print("balance :",self.bal)

s=son()
s.getdata()
s.printdata()
