class student:
    id=int(input("enter id :"))
    name=input("enter name :")

    def getdata(self):
        print(self.id)
        print(self.name)

s=student()
s.getdata()