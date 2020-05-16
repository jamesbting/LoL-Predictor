from DataSetMaker import DataSetMaker
import csv
import cProfile
import pstats
import io

def main():
    region = 'na1'
    api_key_location = "api_key.txt"
    f = open(api_key_location,"r")
    api_key = f.readline()
    f.close()
    ON_DESKTOP = True
    
    if(ON_DESKTOP):
        training_data_location = "C:\\Users\\UserD\\OneDrive - McGill University\\Personal\\Personal Projects\\LoL-Predictor\\datasets\\training_data.csv"
    else:
        training_data_location = "C:\\Users\\James Ting\\OneDrive - McGill University\\Personal\\Personal Projects\\LoL-Predictor\\datasets\\training_data.csv"
    
    #read the last line of the training data, and then set as seed matchID
    mylist = []
    with open(training_data_location,"r") as f:
        for row in reversed(list(csv.reader(f))):
            mylist = row
            break

    starting_matchID = mylist[0] #Seed matchID
    
    num_data_points = 3

    pr = cProfile.Profile()
    pr.enable()
    data_set_maker = DataSetMaker(api_key_location,region,training_data_location,starting_matchID,num_data_points=num_data_points)
    data_set_maker.makeTrainingData()
    pr.disable()
    pr.dump_stats("../cProfile-Results.txt")

if __name__ == "__main__":
    main()