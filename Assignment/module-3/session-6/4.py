
class influencer:
    def influe(self,username,followers):
        print("username :",username)
        print("follwers :",followers)

class brand:
    def brand1(self,brand_name):
        print("brand name :",brand_name)

class brandpartner(influencer,brand):
    def show(self):
        self.influe(self.username,self.followers)
        self.brand1(self.brand_name)

b=brandpartner()
b.username=input("enter username :")
b.followers=int(input("enter followers :"))
b.brand_name=input("enter brand name :")

b.show()
