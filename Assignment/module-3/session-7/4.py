class Content:
    def display(self, title):
        print("Title:", title)
class Movie(Content):
    def display(self, title, year):
        print("Title:", title)
        print("Year:", year)
m = Movie()
m.display("Inception", 2010)