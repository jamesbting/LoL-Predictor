import csv

class DataSetValidator():
    
    def __init__(self,filename):
        self.filename = filename

    def validateDataSet(self):
        repeatedIDs = self.__checkUniqueness()
        if(repeatedIDs == set()):
            print("Every matchID is unique!")
        else:
            print("The following matchIDs are repeated:")
            print(repeatedIDs)
    
    def __checkUniqueness(self):
        matchIDs = set()
        nonUniqueIDs = set()
        with open(self.filename,"r") as f:
            reader = csv.reader(f,delimiter = ',')
            for row in reader:
                matchID = row[0]
                if (matchID in matchIDs):
                    if matchID not in nonUniqueIDs:
                        nonUniqueIDs.add(matchID)
                else:
                    matchIDs.add(matchID)
        return nonUniqueIDs