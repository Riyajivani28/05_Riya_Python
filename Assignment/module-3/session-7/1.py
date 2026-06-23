class InstaStory:
    def share(self):
        print("Sharing an image story")

class WhatsAppStory(InstaStory):
    def share(self):
        print("Sharing a text status")

insta = InstaStory()
whatsapp = WhatsAppStory()

insta.share()
whatsapp.share()