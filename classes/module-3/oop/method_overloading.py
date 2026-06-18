class student:
    def getdata(self,id):
        print("id :",id)

    def getdata(self,name):
        print("name :",name)

s=student()
s.getdata("riya")
s.getdata(111)#python does not support method overloading