from DataSetMaker import DataSetMaker
def main():
    region = 'na1'
    api_key_location = "api_key.txt"
    f = open(api_key_location,"r")
    api_key = f.readline()
    f.close()
    training_data_location = "C:\\Users\\James Ting\\OneDrive - McGill University\\Personal\\Personal Projects\\LoL-Predictor\\datasets\\training_data.csv"
    starting_summ_name = "Falconshot33" #Seed Summoner
    num_data_points = 30
    data_set_maker = DataSetMaker(api_key_location,region,training_data_location,starting_summ_name,num_data_points=num_data_points)
    data_set_maker.makeTrainingData()
if __name__ == "__main__":
    main()