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

    def mainMenu(self):
        while(True):
            print("[MAIN MENU]")
            print("Options:")
            print("[1][System Generator")
            print("[2][Content Generator")
            print("[3][Power Generator")
            print("[4][Economy Generator")
            print()
            print("[5][Save & Quit")
            print()

            userChoice = self.grabInput("CHOOSE");
            while (not self.checkValid(self.populateOptions(5), userChoice)):
                userChoice = self.grabInput("CHOOSE")

            if(userChoice == 1):
                self.systemGen.start()
            elif(userChoice == 2):
                self.contentGen.start()
            elif(userChoice == 4):
                self.economyGen.start()
            elif(userChoice == 5):
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

    def update(self):
        pass
