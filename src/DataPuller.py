from riotwatcher import LolWatcher,ApiError

class AbstractDataPuller:
    #abstract data puller class
    #allows me to create more concrete data pullers that pull data from the API for
    #various types of data (match , player, champion etc)
    def __init__(self,api_key,region):
        self.api_key = api_key
        self.region = region
        self.lol_watcher = LolWatcher(self.api_key)

    def set_api_key(self, new_key):
        self.api_key = new_key

    def set_region(self,new_region):
        self.region = new_region
            

class PlayerDataPuller(AbstractDataPuller):
    #concrete subclass of abstract data puller,
    #pulls player data with various methods, such as account ID, player ID, summoner name, and summoner ID
    def __init__(self,api_key,region):
        super().__init__(api_key,region)
        
    def getPlayerInfoByAccountID(self,accountID):
        return self.lol_watcher.summoner.by_account(self.region,accountID)
        
           

    def getPlayerInfoBySummonerID(self,summonerID):
        return self.lol_watcher.summoner.by_account(self.region,summonerID)
        
           

    def getPlayerInfoBySummonerName(self,summonerName):
        return self.lol_watcher.summoner.by_name(self.region,summonerName)
        
           

    def getPlayerInfoByPlayerID(self,playerID):
        return self.lol_watcher.summoner.by_puuid(self.region,playerID)
    


class MatchDataPuller(AbstractDataPuller):
    #concrete game puller class that pulls data for matches
    def __init__(self,api_key,region):
        super().__init__(api_key,region)
    def getMatchInfoByMatchID(self,matchID):
        return self.lol_watcher.match.by_id(self.region,matchID)
        
           
    
    def getMatchListByAccountID(self,accountID,queue = None,season = None):
        return self.lol_watcher.match.matchlist_by_account(self.region,accountID,queue,season)


class ChampionMasteryDataPuller(AbstractDataPuller):
    def __init__(self,api_key,region):
        super().__init__(api_key,region)

    def getChampionMastery(self,summonerID,championID):
        return self.lol_watcher.champion_mastery.by_summoner_by_champion(self.region,summonerID,championID)
        
           
    
    def getTotalChampionMastery(self,summonerID):
        return self.lol_watcher.champion_mastery.scores_by_summoner(self.region,summonerID)
    