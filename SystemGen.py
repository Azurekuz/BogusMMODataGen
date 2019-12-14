from objects import Region, Server, UserAccount
import os, random
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
        self.generateRegions("sql/regions.sql")

    def generateRegions(self, filePath):
        regionConfig = open("config/regions.txt", "r")
        regionLine = regionConfig.readline().rstrip('\n')
        id = 0
        while regionLine:
            self.regions.append(Region.Region(id, regionLine))
            #print(self.regions[len(self.regions)-1].toString())
            id = id + 1
            regionLine = regionConfig.readline().rstrip('\n')
        if os.path.exists(filePath):
            os.remove(filePath)
        for i in range(0, len(self.regions)):
            self.sqlmaker.insertify("Regions", self.regions[i].getAttributes(), filePath)
        regionConfig.close();

    def generateServers(self, filePath):
        serverConfig = open("config/regions.txt", "r")
        serverLine = serverConfig.readline().rstrip('\n')
        id = 0
        while serverLine:
            self.servers.append(Region.Region(id, serverLine))
            # print(self.regions[len(self.regions)-1].toString())
            id = id + 1
            serverLine = serverConfig.readline().rstrip('\n')
        if os.path.exists(filePath):
            os.remove(filePath)
        for i in range(0, len(self.regions)):
            self.sqlmaker.insertify("Servers", self.servers[i].getAttributes(), filePath)
        serverConfig.close();

    def generateUsers(self):
        pass

    def genUserExpansions(self):
        pass

    def genRanDate(self, minYear, maxYear):
        curYear = random.randint(minYear, maxYear);
        dayMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        if(curYear % 4 == 0):
            dayMonths[1] = 29

        curMonth = random.randint(1, 12);
        curDay = random.randint(1, dayMonths[curMonth-1])

        curYear = self.zeroify(curYear, 4)
        curMonth = self.zeroify(curMonth, 2)
        curDay = self.zeroify(curDay, 2)


        return (curYear + "-" + curMonth + "-" + curDay)

    def zeroify(self, datePart, requiredLength):
        newDatePart = str(datePart)
        if len(newDatePart) < requiredLength:
            for i in range(0, (requiredLength-len(newDatePart))):
                newDatePart = str(0) + newDatePart
        return newDatePart