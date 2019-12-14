from objects import Region, Server, UserAccount, PlayerCharacter
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
        self.generateServers("sql/servers.sql")
        self.generateUsers("sql/users.sql", 10000)
        #self.genPlayerCharacters("sql/playerCharacters.sql", 30000)

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

    def generateServers(self, filePath, limit=25):
        serverConfig = open("config/servers.txt", "r")
        serverLine = serverConfig.readline().rstrip('\n')
        id = 0
        serverNum = limit
        serverNames = []
        while serverLine:
            # print(self.regions[len(self.regions)-1].toString())
            serverNames.append(serverLine)
            serverLine = serverConfig.readline().rstrip('\n')
        usedServerNames = []
        while serverNum > 0:
            ranServer = random.randint(0, len(serverNames)-1)
            while ranServer in usedServerNames:
                ranServer = random.randint(0, len(serverNames)-1)
            self.servers.append(Server.Server(id, random.randint(0, len(self.regions) - 1), serverNames[ranServer]))
            usedServerNames.append(ranServer)
            id = id + 1
            serverNum = serverNum - 1
        if os.path.exists(filePath):
            os.remove(filePath)
        for i in range(0, len(self.servers)):
            self.sqlmaker.insertify("Servers", self.servers[i].getAttributes(), filePath)
        serverConfig.close();

    def generateUsers(self, filePath, limit):
        userConfig = open("config/usernames.txt", "r")
        userLine = userConfig.readline().rstrip('\n')
        usernames = []
        usernameUse = {}
        passwords = []
        numUsers = limit
        id = 0
        while userLine:
            if(len(userLine) >= 6 and len(userLine) < 17):
                usernames.append(userLine)
                usernameUse[userLine] = None
            userLine = userConfig.readline().rstrip('\n')
        userConfig.close();

        userConfig=open("config/passwords.txt")
        userLine = userConfig.readline().rstrip('\n')
        while userLine:
            passwords.append(userLine)
            userLine = userConfig.readline().rstrip('\n')
        userConfig.close();

        for i in range(0, len(usernames)):
            self.users.append(UserAccount.UserAccount(id, usernames[i], passwords[random.randint(0, len(passwords)-1)], self.genRanDate(2002, 2019)))
            id = id + 1
            numUsers = numUsers - 1
            usernameUse[usernames[i]] = 0
            if(numUsers <= 0):
                break

        while numUsers > 0:
            ranUsername = usernames[random.randint(0, len(usernames)-1)]
            if ranUsername in usernameUse.keys():
                self.users.append(UserAccount.UserAccount(id, ranUsername[0:len(ranUsername)-len(str(usernameUse[ranUsername]))]+str(usernameUse[ranUsername]),
                                                          passwords[random.randint(0, len(passwords) - 1)],
                                                          self.genRanDate(2002, 2019)))
                usernameUse[ranUsername] = usernameUse[ranUsername]+1
            id = id + 1
            numUsers = numUsers - 1
        if os.path.exists(filePath):
            os.remove(filePath)
        for i in range(0, len(self.users)):
            self.sqlmaker.insertify("Users", self.users[i].getAttributes(), filePath)

    def genPlayerCharacters(self, filePath, limit):
        playerConfig = open("config/playernames.txt", "r")
        playerLine = playerConfig.readline().rstrip('\n')
        numPlayers = limit
        playerNames = []


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