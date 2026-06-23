
class user:
    pass

class Influencer(user):
    def show(self):
        print("username :",self.username)
        print("email :",self.email)
        print("followers :",self.follwers)
i=Influencer()
i.username=input("enter username :")
i.email=input("enter email :")
i.follwers=int(input("enter follwers :"))

i.show()