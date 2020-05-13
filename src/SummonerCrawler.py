from DataPuller import AbstractDataPuller,PlayerDataPuller,MatchDataPuller
import random

class SummonerCrawler(AbstractDataPuller):
    #essentially an iterator that will return the next summoner name
    #helper class to DataSetMaker
    def __init__(self,api_key,region,starting_summoner_name,iterations = 10000):
        super().__init__(api_key,region)
        self.curr_summoner_name = starting_summoner_name
        self.iterations = iterations
        self.match_puller = MatchDataPuller(self.api_key,self.region)
        self.player_puller = PlayerDataPuller(self.api_key,self.region)

    def hasNext(self):
        return (self.iterations > 0)

    def next(self):
        assert self.hasNext()
        curr_player_matches = self.__getMatchData(self.curr_summoner_name)
        for match in curr_player_matches["matches"]:
            match_id = match['gameId']
            match_data = self.match_puller.getMatchInfoByMatchID(match_id)
            participants = match_data["participantIdentities"]
            
            next_summoner = random.choice(participants)
            next_summoner_name = next_summoner["player"]["summonerName"]
            next_summoner_match_list = self.__getMatchData(next_summoner_name)
            if next_summoner_match_list:
                self.curr_summoner_name = next_summoner_name
                break

        self.iterations += 1
        return next_summoner_name

    def __getMatchData(self,summonerName):
        curr_player = self.player_puller.getPlayerInfoBySummonerName(self.curr_summoner_name)
        return self.match_puller.getMatchListByAccountID(curr_player['accountId'],[420],[13]) #ranked queue only, for the 2019 season

def main():
    region = 'na1'
    f = open("api_key.txt","r")
    api_key = f.readline()
    f.close()
    starting_summ_name = "MisterBentley"
    crawler = SummonerCrawler(api_key,region,starting_summ_name,iterations=3)
    print(crawler.hasNext())
    print(crawler.next())

#main()
