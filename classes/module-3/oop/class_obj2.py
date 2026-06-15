class student:
    id=0
    name=''

    def getdata(self):
        self.id=int(input("enter id "))
        self.name=input("enter name ")

    def printdata(self):
        print("id :",self.id)
        print("name :",self.name)

s=student()
s.getdata()
s.printdata()