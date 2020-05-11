from DataPuller import PlayerDataPuller, MatchDataPuller,ChampionMasteryDataPuller
#file to test other files
class DataPullerTester:
    api_key_location = "api_key.txt"
    f = open(api_key_location)
    api_key = f.readline()
    f.close()
    region = 'na1'
    summonerName = "TheRipsticker" #test pulling my own data
    championID = 21 #champion ID for Miss Fortune
    
    @staticmethod
    def testPlayerDataPuller():
        puller = PlayerDataPuller(DataPullerTester.api_key,DataPullerTester.region)
        
        player_data = puller.getPlayerInfoBySummonerName(DataPullerTester.summonerName)
        print(player_data)
        print(player_data['accountId'])

    @staticmethod
    def testMatchDataPuller():
        player_puller = PlayerDataPuller(DataPullerTester.api_key,DataPullerTester.region)
        match_puller = MatchDataPuller(DataPullerTester.api_key,DataPullerTester.region)
        
        player_data = player_puller.getPlayerInfoBySummonerName(DataPullerTester.summonerName)
        match_timeline_data = match_puller.getMatchListByAccountID(player_data['accountId'])
        print(match_timeline_data)

    @staticmethod
    def testChampionDataPuller():
        player_puller = PlayerDataPuller(DataPullerTester.api_key,DataPullerTester.region)
        champion_puller = ChampionMasteryDataPuller(DataPullerTester.api_key,DataPullerTester.region)
        player_data = player_puller.getPlayerInfoBySummonerName(DataPullerTester.summonerName)
        
        total_champion_data = champion_puller.getTotalChampionMastery(player_data['id'])
        print(total_champion_data)
        champion_data_puller = champion_puller.getChampionMastery(player_data['id'],DataPullerTester.championID)
        print(champion_data_puller)

if __name__ == "__main__":
    DataPullerTester.testPlayerDataPuller()
    DataPullerTester.testMatchDataPuller()
    DataPullerTester.testChampionDataPuller()