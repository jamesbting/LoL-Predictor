from DataSetMaker import DataSetMaker
import csv

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
    
    list = []
    with open(training_data_location,"r") as f:
        list = reversed(list(csv.reader(f)))
    
    starting_matchID = list[0][0] #Seed matchID
    
    num_data_points = 50

    data_set_maker = DataSetMaker(api_key_location,region,training_data_location,starting_matchID,num_data_points=num_data_points)
    data_set_maker.makeTrainingData()

if __name__ == "__main__":
    main()