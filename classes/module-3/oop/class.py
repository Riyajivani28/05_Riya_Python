class student:
    id=1
    name='Riya'

    def getdata(self):
        print("This is part execute")

    def sum(self,a,b):
        print("sum :",a+b)

s=student()
print("id :",s.id)
print("name :",s.name)
s.sum(10,2)
s.getdata()