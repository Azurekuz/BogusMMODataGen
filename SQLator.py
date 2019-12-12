import os
class SQLator:
    def __init__(self):
        pass


    def insertify(self, tableName, valueArray, filePath):
        curFile = open(filePath, "a")

        insertSQL = "INSERT INTO " + tableName + " VALUES("
        for i in range(0, len(valueArray)):
            if(i != len(valueArray)-1):
                insertSQL = insertSQL + str(valueArray[i]) + ","
            else:
                insertSQL = insertSQL + str(valueArray[i]) + ");"
        curFile.write(insertSQL + '\n')