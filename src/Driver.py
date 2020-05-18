from DataSetMaker import DataSetMaker
from SummonerCrawler import SummonerCrawler
from ValidateDataSet import DataSetValidator
from DataPuller import MatchDataPuller
import csv
import io
import time
import random

   

def makeData(training_data_location,writeToColumns = False):
    region = 'na1'
    api_key_location = "api_key.txt"
    f = open(api_key_location,"r")
    api_key = f.readline()
    f.close()
    
    

    num_data_points = 3
    num_data_batches = 10

    matchID_list = set()
    with open(training_data_location,"r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            matchID_list.add(row[0])
        starting_matchID = row[0]
    f.close()
    match_iterator = SummonerCrawler(api_key,region,starting_matchID,max_iterations=num_data_batches*num_data_batches)
    data_set_maker = DataSetMaker(api_key_location,region,training_data_location,match_iterator)

    if(writeToColumns):
        writeColumns()
    
    setNewMatchID = data_set_maker.setNewStartingID
    sleep = time.sleep
    makeData = data_set_maker.makeTrainingData
   
    for batch in range(num_data_batches):
        try:
            starting_matchID = makeData(num_data_points,starting_matchID)
            matchID_list.add(starting_matchID)
            sleep(60)
        except:
            starting_matchID = random.sample(matchID_list,1)[0]
            sleep(60)

def validateData(training_data_location):
    validator = DataSetValidator(training_data_location)
    validator.validateDataSet()

def writeColumns():
    f = open("C:\\Users\\James Ting\\OneDrive - McGill University\\Personal\\Personal Projects\\LoL-Predictor\\docs\\columns.csv","w")
    f.write(str(DataSetMaker.columns))
    f.close()

def main():
    ON_DESKTOP = False
    VALIDATE_DATA = False
    WRITE_TO_COLUMNS = False

    api_key_location = "api_key.txt"
    f = open(api_key_location,"r")
    api_key = f.readline()
    f.close()

    if(ON_DESKTOP):
        training_data_location = "C:\\Users\\UserD\\OneDrive - McGill University\\Personal\\Personal Projects\\LoL-Predictor\\datasets\\training_data.csv"
    else:
        training_data_location = "C:\\Users\\James Ting\\OneDrive - McGill University\\Personal\\Personal Projects\\LoL-Predictor\\datasets\\training_data.csv"
    
    if(VALIDATE_DATA):
        validateData(training_data_location)
    else:
        makeData(training_data_location,WRITE_TO_COLUMNS)
        validateData(training_data_location)
        


if __name__ == "__main__":
    main()