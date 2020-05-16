from DataPuller import AbstractDataPuller,PlayerDataPuller,MatchDataPuller
import random
import time

class SummonerCrawler(AbstractDataPuller):
    #essentially an iterator that will return the next summoner name
    #helper class to DataSetMaker
    exclude_characters = ["í","è",'á','Á','à','À','â','Â','ä','Ä','ã','Ã','å','Å','æ',
                          'Æ','ç','Ç','é','É','è','È','ê','Ê','ë','Ë','í','Í','ì','Ì',
                          'î','Îï','Ï','ñ','Ñ','ó','Ó','ò','Ò','ô','Ô','ö','Ö','õ','Õ',
                          'ø','Ø','œ','Œ','ß','ú','Ú','ù','Ù','û','Û','ü','Ü']
    def __init__(self,api_key,region,starting_matchID,iterations = 10000,rate_limit = 100, num_calls = 8):
        super().__init__(api_key,region)
        self.current_matchID = starting_matchID
        self.max_iterations = iterations
        self.num_iterations = 0
        self.match_puller = MatchDataPuller(self.api_key,self.region)
        self.player_puller = PlayerDataPuller(self.api_key,self.region)
        self.rate_limit = rate_limit
        self.num_calls = num_calls

    #check if there should be a next element (this will essentially limit how many match data points we will have)
    def hasNext(self):
        return self.num_iterations < self.max_iterations

    def next(self,worked = True):
        assert self.hasNext()
        
        #make sure we dont exceed the limit
        #if(self.num_iterations != 0 and (self.num_calls * self.num_iterations) % self.rate_limit == 0):
           # time.sleep(60)

        match_data_list = self.getMatchList()
        all_matches_list = match_data_list["matches"]
        self.current_matchID = random.choice(all_matches_list)["gameId"]
            
            
        if worked:
            self.num_iterations += 1
        return self.current_matchID

    def __getMatchData(self, matchID):
        return self.match_puller.getMatchInfoByMatchID(matchID)

    def getMatchList(self):
        curr_summoners = self.__getMatchData(self.current_matchID)["participantIdentities"]
        for summoner in curr_summoners:
            curr_player = self.player_puller.getPlayerInfoBySummonerName(summoner["player"]["summonerName"])
            try:
                match_data_list = self.getMatchListForParticipant(curr_player)
            except TypeError as e:
                continue
            #if the matchlist is non empty, then return it
            if(match_data_list is not None):
                return match_data_list

    def getMatchListForParticipant(self,curr_player):
        match_data = self.match_puller.getMatchListByAccountID(curr_player['accountId'],[420],[13]) #ranked queue only, for the 2019 season
        return match_data
    
