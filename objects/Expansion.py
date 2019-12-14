class Expansion:
    def __init__(self, expansion_id, name):
        self.expansionID = expansion_id
        self.expansionName = name

    def toString(self):
        return ("{" + "ID:" + str(self.expansionID) + " Name:" + str(self.expansionName) + "}")

    def getAttributes(self):
        return [self.expansionID, self.expansionName]
