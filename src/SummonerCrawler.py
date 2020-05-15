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

    #check if there should be a next element (this will essentially limit how many match data points we will have)
    def hasNext(self):
        return (self.iterations > 0 and self.getMatchData(self.curr_summoner_name) is not None)

    def next(self):
        assert self.hasNext()
        curr_player_matches = self.getMatchData(self.curr_summoner_name)

        for match in curr_player_matches["matches"]:
            match_id = match['gameId']
            match_data = self.match_puller.getMatchInfoByMatchID(match_id)
            if match_data is None:
                continue
            participants = match_data["participantIdentities"]
            
            #get info on the next summoner
            next_summoner = random.choice(participants)
            next_summoner_name = next_summoner["player"]["summonerName"]
            next_summoner_match_list = self.getMatchData(next_summoner_name)

            #if the matchlist is non empty, then a summoner that can be the next summoner has been found
            if next_summoner_match_list:
                self.curr_summoner_name = next_summoner_name
                break

        self.iterations -= 1
        return next_summoner_name

    def getMatchData(self,summonerName):
        curr_player = self.player_puller.getPlayerInfoBySummonerName(self.curr_summoner_name)
        match_data = self.match_puller.getMatchListByAccountID(curr_player['accountId'],[420],[13]) #ranked queue only, for the 2019 season
        return match_data
