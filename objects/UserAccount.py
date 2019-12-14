class UserAccount:
    def __init__(self, user_id, username, password, date):
        self.userID = user_id
        self.userName = username
        self.password = password
        self.dateCreated = date

    def toString(self):
        return ("{" + "ID:" + str(self.userID) + " Name:" + str(self.userName) + " Password:" + self.password + " Created:" + self.dateCreated +  "}")

    def getAttributes(self):
        return [self.userID, self.userName, self.password, self.dateCreated];
