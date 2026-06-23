
class student:
    def display(self,username,email):
        print("username :",username)
        print("email :",email)

u=input("enter username :")
e=input("enter email :")

s=student()
s.display(u,e)