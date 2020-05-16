from DataSetMaker import DataSetMaker
from SummonerCrawler import SummonerCrawler
import csv
import io
import time

def main():
    region = 'na1'
    api_key_location = "api_key.txt"
    f = open(api_key_location,"r")
    api_key = f.readline()
    f.close()
    ON_DESKTOP = False
    
    if(ON_DESKTOP):
        training_data_location = "C:\\Users\\UserD\\OneDrive - McGill University\\Personal\\Personal Projects\\LoL-Predictor\\datasets\\training_data.csv"
    else:
        training_data_location = "C:\\Users\\James Ting\\OneDrive - McGill University\\Personal\\Personal Projects\\LoL-Predictor\\datasets\\training_data.csv"
    
   
    num_data_points = 2
    num_data_batches = 30
    mylist = []
    with open(training_data_location,"r") as f:
        for row in reversed(list(csv.reader(f))):
            mylist = row
            break
    starting_matchID = mylist[0]
    match_iterator = SummonerCrawler(api_key,region,starting_matchID,iterations=num_data_batches*num_data_batches)
    data_set_maker = DataSetMaker(api_key_location,region,training_data_location,match_iterator)
    setNewMatchID = data_set_maker.setNewStartingID
    sleep = time.sleep
    makeData = data_set_maker.makeTrainingData

    for batch in range(num_data_batches):

        starting_matchID = makeData(num_data_points,starting_matchID)
        
        #read the last line of the training data, and then set as seed matchID
        #mylist = []
        #with open(training_data_location,"r") as f:
            #for row in reversed(list(csv.reader(f))):
             #   mylist = row
             #   break
        starting_matchID = mylist[0]
        
        
    

if __name__ == "__main__":
    main()