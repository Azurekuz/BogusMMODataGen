class Quest:
    def __init__(self, quest_id, name, npc_id):
        self.questID = quest_id
        self.questName = name
        self.npcID = npc_id

    def toString(self):
        return ("{" + "ID:" + str(self.questID) + " Name:" + str(self.questName) + "NPC:" + self.npcID + "}")

    def getAttributes(self):
        return [self.questID, self.questName, self.npcID];