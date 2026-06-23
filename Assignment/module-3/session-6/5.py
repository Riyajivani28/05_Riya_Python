class user:
    pass

class influencer(user):
    pass

class VerifiedInfluencer(influencer):
    def display_profile(self):
        print("Username :", self.username)

        if self.followers >= 1000:
            print("Followers :", self.followers / 1000, "K")
        else:
            print("Followers :", self.followers)

        print("Badge :", self.badge)

v = VerifiedInfluencer()

v.username = input("Enter Username : ")
v.followers = int(input("Enter Followers : "))
v.badge = input("Enter Badge : ")

v.display_profile()