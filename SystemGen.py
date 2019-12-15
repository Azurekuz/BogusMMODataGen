from objects import Region, Server, UserAccount, PlayerCharacter, AuctionEntry, AuctionBid
import os, random
import SQLator
#24 by 36 inch poster
class SystemGen:
    def __init__(self):
        self.regions = []
        self.servers = []
        self.users = []
        self.playerCharacters = []
        self.hasExpansions = []
        self.auctionEntries = []
        self.auctionBids = []
        self.sqlmaker = SQLator.SQLator()

    def resetLists(self):
        self.regions[:] = []
        self.servers[:] = []
        self.users[:] = []
        self.playerCharacters[:] = []
        self.auctionEntries[:] = []
        self.auctionBids[:] = []

    def start(self):
        print("[SYSTEM GENERATOR]")
        self.resetLists()
        self.generateRegions("sql/regions.sql")
        self.generateServers("sql/servers.sql")
        self.generateUsers("sql/users.sql", 10000)
        self.genPlayerCharacters("sql/playerChar.sql", 30000)
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
            self.users.append(UserAccount.UserAccount(id, usernames[i], passwords[random.randint(0, len(passwords)-1)], self.genRanDate(2018, 2019)))
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
        usedPlayerNames = {}
        id = 0
        while(playerLine):
            if (len(playerLine) >= 6 and len(playerLine) < 17):
                playerNames.append(playerLine)
                usedPlayerNames[playerLine] = None
            playerLine = playerConfig.readline().rstrip('\n')

        for i in range(0, len(playerNames)):
            self.playerCharacters.append(PlayerCharacter.PlayerCharacter(id, playerNames[i], random.randint(0, len(self.servers)-1), random.randint(0, len(self.users)-1)))
            id = id + 1
            numPlayers = numPlayers - 1
            usedPlayerNames[playerNames[i]] = 0
            if(numPlayers <= 0):
                break

        while numPlayers > 0:
            ranName = playerNames[random.randint(0, len(playerNames)-1)]
            if ranName in usedPlayerNames.keys():
                self.playerCharacters.append(UserAccount.UserAccount(id, ranName[0:len(ranName)-len(str(usedPlayerNames[ranName]))]+str(usedPlayerNames[ranName]),
                                                          random.randint(0, len(self.servers) - 1),
                                                          random.randint(0, len(self.users)-1)))
                usedPlayerNames[ranName] = usedPlayerNames[ranName]+1
                numPlayers = numPlayers - 1
                id = id + 1
        if os.path.exists(filePath):
            os.remove(filePath)
        for i in range(0, len(self.playerCharacters)):
            self.sqlmaker.insertify("PlayerCharacter", self.playerCharacters[i].getAttributes(), filePath)


    def genUserExpansions(self, filePath, expansions):
        for i in range(0, len(self.users)):
            ranExpansionNum = random.randint(1, len(expansions)-1)
            for ii in range(0, ranExpansionNum):
                self.hasExpansions.append([i, ii])
        if os.path.exists(filePath):
            os.remove(filePath)
        for i in range(0, len(self.hasExpansions)):
            self.sqlmaker.insertify("HasExpansion", [self.hasExpansions[0], self.hasExpansions[1]], filePath)

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

    def genAuctionHouse(self, items, filePath, approxlimit):
        id = 0
        numEntries = approxlimit
        for i in range(0,len(self.playerCharacters)):
            entries = random.randint(1,3)
            if(random.randint(0, 100) > 45):
                while(entries > 0):
                    price = random.randint(10, 999999999)
                    self.auctionEntries.append(AuctionEntry.AuctionEntry(id, random.randint(0, len(items)-1), price,
                                                                         price*random.randint(2,5),
                                                                         random.randint(0, len(self.playerCharacters)-1)));
                    entries = entries - 1
                    numEntries = numEntries - 1
                    id = id + 1
            if numEntries <= 0:
                break
        if os.path.exists(filePath):
            os.remove(filePath)
        for i in range(0, len(self.auctionEntries)):
            self.sqlmaker.insertify("AuctionHouse", self.auctionEntries[i].getAttributes(), filePath)

    def genAuctionBids(self, filePath, items, limit):
        id = 0
        numBids = limit
        for i in range(0,len(self.playerCharacters)):
            entries = random.randint(1,3)
            ranEntry = random.randint(0, len(self.auctionEntries)-1)
            if(random.randint(0, 100) > 45 and self.auctionEntries[ranEntry].playerID != self.playerCharacters[i] and self.auctionEntries[ranEntry].serverID == self.playerCharacters[i].serverID):
                while(entries > 0):
                    price = random.randint(10, 999999999)
                    self.auctionEntries.append(AuctionEntry.AuctionEntry(id, random.randint(0, len(self.playerCharacters)-1), price,
                                                                         self.auctionEntries[ranEntry].startPrice + random.randint(1, self.auctionEntries[ranEntry].startPrice*1.5),
                                                                         ranEntry));
                    entries = entries - 1
                    numBids = numBids - 1
                    id = id + 1