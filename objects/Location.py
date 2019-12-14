class Location:
    def __init__(self, location_id, name, expansion_id):
        self.locationID = location_id
        self.locationName = name
        self.expansionID = expansion_id

    def toString(self):
        return ("{" + "ID:" + str(self.locationID) + " Name:" + str(self.locationName) + "}")

    def getAttributes(self):
        return [self.locationID, self.locationName, self.expansionID]