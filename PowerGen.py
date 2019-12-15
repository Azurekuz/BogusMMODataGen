from objects import Guild
import os, random
import SQLator
class PowerGen:
    def __init__(self):
        self.guilds = []
        self.guildMembers = []

        self.guildMasters = []
        self.memberChar = []
        self.sqlmaker = SQLator.SQLator()

    def start(self, ):
        pass

    def resetLists(self):
        self.guilds[:] = []
        self.guildMembers[:] = []

        self.guildMasters[:] = []
        self.memberChar[:] = []

    def genGuilds(self, filePath, players):
        "\t" + "[GEN GUILDS]"
        guildConfig = open("config/guilds.txt", "r")
        guildLine = guildConfig.readline().rstrip('\n')
        guilds = []
        id = 0
        while guildLine:
            guilds.append(guildLine)

        for i in range(0, len(self.guilds)):
            ranMaster = random.randint(0, len(players)-1)
            while ranMaster in self.guildMasters:
                ranMaster = random.randint(0, len(players) - 1)
            self.guilds.append(Guild.Guild(id, guildLine, ranMaster))
            id = id + 1
            self.guildMasters.append(ranMaster)
            guildLine = guildConfig.readline().rstrip('\n')
        if os.path.exists(filePath):
            os.remove(filePath)
        for i in range(0, len(self.guilds)):
            self.sqlmaker.insertify("Guilds", self.guilds[i].getAttributes(), filePath)
        guildConfig.close();

    def addGuildMembers(self, filePath, players):
        print("\t" + "[ADD GUILD MEMBERS]")
        for i in range(0, len(players)):
            if(random.randint(0,100) > 45 and players[i] not in self.guildMasters):
                self.sqlmaker.insertify("GuildMembers", [self.guilds[random.randint(0, len(self.guilds)-1)], players[i]], filePath)
