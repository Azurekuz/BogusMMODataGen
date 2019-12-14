class NPC:
    def __init__(self, npc_id, name, location_id):
        self.npcID = npc_id
        self.npcName = name
        self.locationID = location_id

    def toString(self):
        return ("{" + "ID:" + str(self.npcID) + " Name:" + str(self.npcName) + " LocID:" + str(self.locationID)+ "}")

    def getAttributes(self):
        return [self.npcID, self.npcName, self.locationID]