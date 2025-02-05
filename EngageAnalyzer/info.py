class Info:
    def __init__(self, creator, user, subject, contents):
        self.creator = creator
        self.user = user
        self.subject = subject
        self.contents = contents
    
    def printInfo(self):
        print(f"{self.creator}, {self.user}: {self.subject} {self.contents}")

    