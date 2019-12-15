from objects import Expansion, Location, NPC, Quest
import os, random
import SQLator
class ContentGen:
    def __init__(self):
        self.expansions = []
        self.locations = []
        self.NPCs = []
        self.quests = []
        self.questRewards = []
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
        self.genQuests("sql/quests.sql", 1000)

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
                #print(self.NPCs[len(self.NPCs)-1].toString())
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

    def genQuests(self, filePath, limit=0):
        questConfig = open("config/quests.txt", "r")
        questLine = questConfig.readline().rstrip('\n')
        id = 0
        quests = []
        numQuests = limit;
        questParts = {};
        while questLine:
            if questLine[0] != " " or questLine[0] != "":
                self.quests.append(Quest.Quest(id, questLine, random.randint(0, len(self.NPCs)-1)))
                # print(self.regions[len(self.regions)-1].toString())
                id = id + 1
                quests.append(questLine)
                questParts[questLine] = 2
                numQuests = numQuests - 1
                questLine = questConfig.readline().rstrip('\n')

        while numQuests > 0:
            ranQuest = quests[random.randint(0, len(quests)-1)];
            self.quests.append(Quest.Quest(id, ranQuest + " " + str(questParts[ranQuest]), random.randint(0, len(self.NPCs) - 1)))
            id = id + 1
            numQuests = numQuests - 1
            questParts[ranQuest] = questParts[ranQuest] + 1
        if os.path.exists(filePath):
            os.remove(filePath)
        for i in range(0, len(self.quests)):
            self.sqlmaker.insertify("Quests", self.quests[i].getAttributes(), filePath)
        questConfig.close();

    def completeQuests(self, filePath, players):
        questCompletion = {}
        if os.path.exists(filePath):
            os.remove(filePath)
        for i in range(0, len(players)):
            questCompletion = []
            ranNum = random.randint(0, 20)
            while ranNum in questCompletion:
                ranNum = random.randint(0, len(self.quests) - 1)
            while ranNum > 0:
                self.sqlmaker.insertify("QuestComplete", [i, random.randint(0, len(self.quests)-1)], filePath)
                ranNum = ranNum - 1
                questCompletion.append(ranNum)

    def genQuestRewards(self, filePath, items, limit=0):
        if os.path.exists(filePath):
            os.remove(filePath)
        for i in range(0, len(self.quests)):
            self.sqlmaker.insertify("QuestReward", [i, random.randint(0, len(items)-1)], filePath)