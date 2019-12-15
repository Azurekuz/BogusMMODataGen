import SystemGen
import ContentGen
import PowerGen
import EconomyGen
import objects

class MMOGenNexus:
    userName = None

    def __init__(self):
        self.systemGen = SystemGen.SystemGen()
        self.contentGen = ContentGen.ContentGen()
        self.powerGen = PowerGen.PowerGen()
        self.economyGen = EconomyGen.EconomyGen()

    def start(self):
        print("[WELCOME TO THE MMO BOGUS DATA GENERATOR]");
        print("[Your name?][ ", end='')
        userName = input()
        print("Welcome " + userName + "!")
        print()
        self.mainMenu()

    def generateAll(self):
        print(["[GENERATE ALL]"])
        self.resetAll()

        self.systemGen.generateRegions("sql/regions.sql")
        self.systemGen.generateServers("sql/servers.sql")
        self.systemGen.generateUsers("sql/users.sql", 100)
        self.economyGen.genItems("sql/items.sql")
        self.contentGen.genExpansions("sql/expansions.sql")
        self.systemGen.genUserExpansions("sql/hasExpansion.sql", self.contentGen.expansions)
        self.contentGen.genLocations("sql/locations.sql")
        self.contentGen.genNPCs("sql/npcs.sql", 800)
        self.contentGen.genQuests("sql/quests.sql", 100)
        self.contentGen.genQuestRewards("sql/questRewards.sql", self.economyGen.items)
        self.systemGen.genPlayerCharacters("sql/playerChar.sql", 300)
        self.contentGen.completeQuests("sql/completeQuests.sql", self.systemGen.playerCharacters)
        self.powerGen.genGuilds("sql/guilds.sql", self.systemGen.playerCharacters)
        self.powerGen.addGuildMembers("sql/guildMembers.sql", self.systemGen.playerCharacters)
        self.systemGen.genAuctionHouse(self.economyGen.items, "sql/auctionHouse.sql", 5000)
        self.systemGen.genAuctionBids("sql/auctionBids.sql", 10000)


    def mainMenu(self):
        while(True):
            print("[MAIN MENU]")
            print("Options:")
            print("[1][System Generator")
            print("[2][Content Generator")
            print("[3][Power Generator")
            print("[4][Economy Generator")
            print()
            print("[5][GENERATE ALL")
            print("[6][Save & Quit")
            print()

            userChoice = self.grabInput("CHOOSE");
            while (not self.checkValid(self.populateOptions(5), userChoice)):
                userChoice = self.grabInput("CHOOSE")

            if(userChoice == 1):
                self.systemGen.start()
            elif(userChoice == 2):
                self.contentGen.start()
                self.contentGen.genQuestRewards("sql/questRewards.sql", self.economyGen.items)
                #self.contentGen.completeQuests("sql/questsComplete.sql", self.systemGen.playerCharacters)
            elif(userChoice == 4):
                self.economyGen.start()
            elif (userChoice == 5):
                self.generateAll()
            elif(userChoice == 6):
                break

    def populateOptions(self, max):
        optionsArray = [];
        for i in range(1, max + 1):
            optionsArray.append(i)
        return optionsArray

    def checkValid(self, validChoiceArray, choice, error="Invalid choice selected!"):
        if choice not in validChoiceArray:
            print("[ERROR][" + error + "]")
            return False
        else:
            return True

    def grabInput(self, prompt):
        print("[" + prompt + "][ ", end='')
        return int(input())

    def resetAll(self):
        self.contentGen.resetLists()
        self.economyGen.resetLists()
        self.systemGen.resetLists()
        self.powerGen.resetLists()

    def update(self):
        pass
