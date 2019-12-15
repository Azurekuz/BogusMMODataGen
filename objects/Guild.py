class Guild:
    def __init__(self, guild_id, name, master_id):
        self.guildID = guild_id
        self.guildName = name
        self.guildMaster = master_id

    def toString(self):
        return ("{" + "ID:" + str(self.guildID) + " Name:" + str(self.guildName) + " GM:" + self.guildMaster + "}")

    def getAttributes(self):
        return [self.guildID, self.guildName, self.guildMaster]