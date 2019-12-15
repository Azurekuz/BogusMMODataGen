from objects import Item, AuctionEntry, AuctionBid
import os
import SQLator
class EconomyGen:
    def __init__(self):
        self.items = []
        self.sqlmaker = SQLator.SQLator()

    def start(self):
        print("[ECONOMY GENERATOR]")
        self.resetLists()
        self.genItems("sql/items.sql")

    def resetLists(self):
        self.items[:] = []

    def genItems(self, filePath):
        print("\t" + "[GEN ITEMS]")
        itemConfig= open("config/items.txt", "r")
        itemLine = itemConfig.readline().rstrip('\n')
        id = 0
        while itemLine:
            self.items.append(Item.Item(id, itemLine))
            #print(self.items[len(self.items) - 1].toString())
            id = id + 1
            itemLine = itemConfig.readline().rstrip('\n')
        if os.path.exists(filePath):
            os.remove(filePath)
        for i in range(0, len(self.items)):
            self.sqlmaker.insertify("Items", self.items[i].getAttributes(), filePath)
        itemConfig.close();