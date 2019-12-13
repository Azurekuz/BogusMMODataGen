class Item:
    def __init__(self, item_id, name):
        self.itemID = item_id
        self.itemName = name

    def toString(self):
        return ("{" + "ID:" + str(self.itemID) + " Name:" + str(self.itemName) + "}")

    def getAttributes(self):
        return [self.itemID, self.itemName];