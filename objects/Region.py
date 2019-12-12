class Region:
    def __init__(self, region_id, name):
        self.regionID = region_id
        self.regionName = name

    def toString(self):
        return ("{" + "ID:" + str(self.regionID) + " Name:" + str(self.regionName) + "}")