'''class stu:
    def __init__(self):
        self.id=int(input("enter id :"))
        self.name=input("enter name :")

    def display(self):
        print("id :",self.id)
        print("name : ",self.name)

s=stu()
s.display()'''


'''import random
class num:
    r=random.randrange(1,100)
    print(r)
n=num()'''

class stu:
    def __init__(self,id,name):
        print("id :",id)
        print("name :",name)
    
id=int(input("enter id :"))
name=input("enter name :")
s=stu(id,name)