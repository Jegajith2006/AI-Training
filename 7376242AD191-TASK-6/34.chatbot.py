class Response:
    def reply(self):
        pass

class Friendly(Response):
    def reply(self):
        print("Hello! How can I help?")

r = Friendly()
r.reply()
