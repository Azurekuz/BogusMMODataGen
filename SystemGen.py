from objects import Region, Server, UserAccount
import SQLator
#24 by 36 inch poster
class SystemGen:
    def __init__(self):
        self.regions = []
        self.servers = []
        self.users = []
        self.sqlmaker = SQLator.SQLator()

    def resetLists(self):
        self.regions[:] = []
        self.servers[:] = []
        self.users[:] = []

    def start(self):
        print("[SYSTEM GENERATOR]")
        self.resetLists()
        self.generateRegions()

    def generateRegions(self):
        regionConfig = open("config/regions.txt", "r")
        regionLine = regionConfig.readline().rstrip('\n')
        id = 0
        while regionLine:
            self.regions.append(Region.Region(id, regionLine))
            print(self.regions[len(self.regions)-1].toString())
            id = id + 1
            regionLine = regionConfig.readline().rstrip('\n')
        for i in range(0, len(self.regions)):
            self.sqlmaker.insertify("Regions", self.regions[i].getAttributes())
        regionConfig.close();

    def generateServers(self):
        pass

    def generateUsers(self):
        pass

    def genUserExpansions(self):
        pass