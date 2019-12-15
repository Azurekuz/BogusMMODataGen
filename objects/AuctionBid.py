class AuctionBid:
    def __init__(self, bid_id, player_id, bid_amt, auction_id):
        self.bidID = bid_id
        self.playerID = player_id
        self.bidAmount = bid_amt
        self.auctionEntryID = auction_id

    def toString(self):
        return ("{" + "ID:" + str(self.bidID) + " Player:" + str(self.playerID) + " Bid Amt:" + self.bidAmount +
                "EntryID:" + self.auctionEntryID + "}")

    def getAttributes(self):
        return [self.guildID, self.guildName, self.guildMaster]