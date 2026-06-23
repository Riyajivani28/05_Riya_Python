class Notification:
    def send(self):
        print("Sending generic notification")
class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")
class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification ")
n1 = EmailNotification()
n2 = SMSNotification()
n1.send()
n2.send()