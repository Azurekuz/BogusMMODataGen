from objects import Region, Server, UserAccount
#24 by 36 inch poster
class SystemGen:
    def __init__(self):
        self.regions = []
        self.servers = []
        self.users = []


    def start(self):
        print("[SYSTEM GENERATOR]")
        self.generateRegions()

    def generateRegions(self):
        try:
            regionConfig = open("config/regions.txt", "r")
            regionLine = regionConfig.readline().rstrip('\n')
            id = 0
            while regionLine:
                self.regions.append(Region.Region(id, regionLine))
                id = id + 1
                regionLine = regionConfig.readline().rstrip('\n')
        finally:
            for i in range(0, len(self.regions)):
                print(self.regions[i].toString())
            regionConfig.close();

    def generateServers(self):
        pass

    def generateUsers(self):
        pass

    def genUserExpansions(self):
        pass