from objects import Expansion, Location, NPC, Quest
import os, random
import SQLator
class ContentGen:
    def __init__(self):
        self.expansions = []
        self.locations = []
        self.NPCs = []
        self.quests = []
        self.sqlmaker = SQLator.SQLator()

    def resetLists(self):
        self.expansions[:] = []
        self.locations[:] = []
        self.NPCs[:] = []
        self.quests[:] = []

    def start(self):
        print("[CONTENT GENERATOR]")
        self.resetLists()
        self.genExpansions("sql/expansions.sql")
        self.genLocations("sql/locations.sql")
        self.genNPCs("sql/npcs.sql", 8000)

    def genExpansions(self, filePath):
        expacConfig = open("config/expansions.txt", "r")
        expacLine = expacConfig.readline().rstrip('\n')
        id = 0
        while expacLine:
            self.expansions.append(Expansion.Expansion(id, expacLine))
            id = id + 1
            expacLine = expacConfig.readline().rstrip('\n')
        if os.path.exists(filePath):
            os.remove(filePath)
        for i in range(0, len(self.expansions)):
            self.sqlmaker.insertify("Expansions", self.expansions[i].getAttributes(), filePath)
        expacConfig.close();

    def genLocations(self, filePath):
        locationConfig = open("config/locations.txt", "r")
        locLine = locationConfig.readline().rstrip('\n')
        id = 0
        while locLine:
            self.locations.append(Location.Location(id, locLine, random.randint(0,len(self.expansions)-1)))
            id = id + 1
            locLine = locationConfig.readline().rstrip('\n')
        if os.path.exists(filePath):
            os.remove(filePath)
        for i in range(0, len(self.locations)):
            self.sqlmaker.insertify("Locations", self.locations[i].getAttributes(), filePath)
        locationConfig.close();

    def genNPCs(self, filePath, limit):
        npcConfig = open("config/npcs.txt", "r")
        npcLine = npcConfig.readline().rstrip('\n')
        resetPos = npcConfig.tell()
        id = 0
        npcInstances = {}
        npcNum = limit
        while npcNum > 0:
            while npcLine:
                if(npcLine not in npcInstances):
                    npcInstances[npcLine] = []
                ranLoc = random.randint(0, len(self.locations)-1)
                while(ranLoc in npcInstances[npcLine] and len(npcInstances[npcLine]) != len(self.locations)):
                    ranLoc = random.randint(0, len(self.locations) - 1)
                npcInstances[npcLine].append(ranLoc);
                self.NPCs.append(NPC.NPC(id, npcLine, ranLoc))
                print(self.NPCs[len(self.NPCs)-1].toString())
                npcNum = npcNum - 1
                id = id + 1
                npcLine = npcConfig.readline().rstrip('\n')
            npcConfig.seek(0)
            npcLine = npcConfig.readline().rstrip('\n')
        if os.path.exists(filePath):
            os.remove(filePath)
        for i in range(0, len(self.NPCs)):
            self.sqlmaker.insertify("NPCs", self.NPCs[i].getAttributes(), filePath)
        npcConfig.close();

    def genQuests(self):
        pass

    def completeQuests(self):
        pass

    def genQuestRewards(self):
        pass