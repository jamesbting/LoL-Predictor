import csv
list = []
training_data_location = "C:\\Users\\James Ting\\OneDrive - McGill University\\Personal\\Personal Projects\\LoL-Predictor\\datasets\\training_data.csv"
with open(training_data_location,"r") as f:
    list = reversed(list(csv.reader(f)))

starting_matchID = list[0][0] #Seed matchID
print(starting_matchID)
