class student:

    def getdata(self,id,name):
        print("id :",id)
        print("name :",name)

s=student()
id=int(input("enter id :"))
name=input("enter name :")
s.getdata(id,name)