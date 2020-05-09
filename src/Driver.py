from DataPuller import PlayerDataPuller, MatchDataPuller
#file to test other files
class DataPullerTester:
    api_key_location = "api_key.txt"
    f = open(api_key_location)
    api_key = f.readline()
    f.close()
    region = 'na1'
    summonerName = "TheRipsticker" #test pulling my own data
    
    @staticmethod
    def testPlayerDataPuller():
        puller = PlayerDataPuller(DataPullerTester.api_key,DataPullerTester.region)
        player_data = puller.getPlayerInfoBySummonerName(DataPullerTester.summonerName)
        print(player_data)

    @staticmethod
    def testMatchDataPuller():
        player_puller = PlayerDataPuller(DataPullerTester.api_key,DataPullerTester.region)
        match_puller = MatchDataPuller(DataPullerTester.api_key,DataPullerTester.region)
        player_data = player_puller.getPlayerInfoBySummonerName(DataPullerTester.summonerName)
        match_timeline_data = match_puller.getMatchListByAccountID(player_data['accountId'])
        print(match_timeline_data)




if __name__ == "__main__":
    DataPullerTester.testPlayerDataPuller()
    DataPullerTester.testMatchDataPuller()