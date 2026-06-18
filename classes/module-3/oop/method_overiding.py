class Website:
    def login(self, usernm, password):
        if usernm == "user" and password == "2865":
            print("Login Successfully")
        else:
            print("Wrong Username or Password")

class Home(Website):
    def login(self, usernm, password):
        print("Home Page")
        super().login(usernm, password)

class About(Website):
    def login(self, usernm, password):
        print("About Page")
        super().login(usernm, password)

class Blog(Website):
    def login(self, usernm, password):
        print("Blog Page")
        super().login(usernm, password)

u = input("Enter Username: ")
p = input("Enter Password: ")

h = Home()
h.login(u, p)

a = About()
a.login(u, p)

b = Blog()
b.login(u, p)