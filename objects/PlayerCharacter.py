class PlayerCharacter:
    def __init__(self, player_id, name, server_id, user_id):
        self.playerID = player_id
        self.playerName = name
        self.serverID = server_id
        self.userID = user_id

    def toString(self):
        return ("{" + "ID:" + str(self.playerID) + " Name:" + str(self.playerName) + " Password:" + self.serverID + " Created:" + self.userID +  "}")

    def getAttributes(self):
        return [self.playerID, self.playerName, self.serverID, self.userID];