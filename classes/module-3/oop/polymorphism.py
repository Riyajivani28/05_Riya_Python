#Ek j method (show()) alag-alag class ma alag rite work kare tene Polymorphism kahe.
class Home:
    def show(self):
        print("Home Page")

class About:
    def show(self):
        print("About Page")

class Blog:
    def show(self):
        print("Blog Page")

h = Home()
a = About()
b = Blog()

for x in (h, a, b):
    x.show()

