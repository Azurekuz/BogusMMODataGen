class Server:
    def __init__(self, server_id, region, name):
        self.serverID = server_id
        self.regionID = region
        self.serverName = name

    def toString(self):
        return ("{" + "ID:" + str(self.serverID) + "RegionID:" + str(self.regionID) + " Name:" + str(self.serverName) + "}")

    def getAttributes(self):
        return [self.serverID, self.regionID, self.serverName];