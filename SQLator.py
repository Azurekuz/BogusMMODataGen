class SQLator:
    def __init__(self):
        pass


    def insertify(self, tableName, valueArray):
        insertSQL = "INSERT INTO " + tableName + " VALUES("
        for i in range(0, len(valueArray)):
            if(i != len(valueArray)-1):
                insertSQL = insertSQL + str(valueArray[i]) + ","
            else:
                insertSQL = insertSQL + str(valueArray[i]) + ");"
        print(insertSQL)