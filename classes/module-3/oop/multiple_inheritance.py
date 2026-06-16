class riya:
    rid:int
    rname:str

    def rgetdata(self):
        self.rid=int(input("enter id :"))
        self.rname=input("enter name :")

class gatu:
     gid:int
     gname:str

     def ggetdata(self):
        self.gid=int(input("enter id :"))
        self.gname=input("enter name :")

class dati:
     did:int
     dname:str

     def dgetdata(self):
        self.did=int(input("enter id :"))
        self.dname=input("enter name :")

class python(riya,gatu,dati):
    def display(self):
        print("-------------riya----------------")
        print("id : ",self.rid)
        print("name :",self.rname)
        print("---------------gatu--------------")
        print("id : ",self.gid)
        print("name : ",self.gname)
        print("----------------dati--------------")
        print("id : ",self.did)
        print("name : ",self.dname)

p=python()
p.rgetdata()
p.ggetdata()
p.dgetdata()
p.display()

    
