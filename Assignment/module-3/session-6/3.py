
'''Demonstrate multilevel inheritance by creating a class 
VerifiedInfluencer that inherits from Influencer and
adds a badge attribute; create a VerifiedInfluencer object and 
display all its properties.'''

class user:
    pass

class influencer(user):
    pass

class VerifiedInfluencer(influencer):
    def show(self):
        print("username :",self.username)
        print("email :",self.email)
        print("follwers :",self.follwers)
        print("badge :",self.badge)

v=VerifiedInfluencer()
v.username=input("enter username :")
v.email=input("enter email :")
v.follwers=int(input("enter followers :"))
v.badge=input("enter badge :")

v.show()