class AuctionEntry:
    def __init__(self, auction_id, item_id, start_price, buy_price, date_created, player_id):
        self.auctionEntryID = auction_id
        self.itemID = item_id
        self.startPrice = start_price
        self.buyPrice = buy_price
        self.dateCreated = date_created
        self.playerID = player_id

    def toString(self):
        return ("{" + "ID:" + str(self.auctionEntryID) + " Item:" + str(self.itemID) + " S.Price:" +
                str(self.startPrice) + " B.Price:" + str(self.buyPrice) + " Date:" + str(self.dateCreated) +
                " Player:" + str(self.playerID) +"}")

    def getAttributes(self):
        return [self.auctionEntryID, self.itemID, self.startPrice, self.buyPrice, self.dateCreated, self.playerID]
