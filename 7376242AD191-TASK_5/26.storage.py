class Storage:
    def __init__(self, limit):
        self.limit = limit

    def upload(self, size):
        if size <= self.limit:
            print("Uploaded")
        else:
            print("Limit Exceeded")

s = Storage(int(input()))
s.upload(int(input()))
