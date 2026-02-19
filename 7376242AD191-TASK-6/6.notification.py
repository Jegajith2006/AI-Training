class Notification:
    def send(self):
        pass

class Email(Notification):
    def send(self):
        print("Email Sent")

class SMS(Notification):
    def send(self):
        print("SMS Sent")

n = Email()
n.send()
