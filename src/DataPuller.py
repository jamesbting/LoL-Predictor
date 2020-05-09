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
    def ApiErrorMessage(self,err):
        if err.response.status_code == 429:
            print(f"We should retry in{err.headers['Retry-After']} seconds")
            print("This retry-after is handled by default by the RiotWatcher library")
            print("Future requests must wait until the retry-after time has passed")
        elif err.response.status_code == 404:
            print(f"No such information could not be found")
        else:
            raise

class PlayerDataPuller(AbstractDataPuller):
    #concretesub class of abstract data puller,
    #pulls player data with various methods, such as account ID, player ID, summoner name, and summoner ID
    def __init__(self,api_key,region):
        super().__init__(api_key,region)
        
    def getPlayerInfoByAccountID(self,accountID):
        try:
            return self.lol_watcher.summoner.by_account(self.region,accountID)
        except ApiError as err:
            ApiErrorMessage(err)

    def getPlayerInfoBySummonerID(self,summonerID):
        try:
            return self.lol_watcher.summoner.by_account(self.region,summonerID)
        except ApiError as err:
            ApiErrorMessage(err)

    def getPlayerInfoBySummonerName(self,summonerName):
        try:
            return self.lol_watcher.summoner.by_name(self.region,summonerName)
        except ApiError as err:
            ApiErrorMessage(err)

    def getPlayerInfoByPlayerID(self,playerID):
        try:
            return self.lol_watcher.summoner.by_puuid(self.region,playerID)
            self.lol_watcher.summoner.by_id
        except ApiError as err:
            ApiErrorMessage(err)

    def ApiErrorMessage(self,err):
        super().ApiErrorMessage(err)
        print("This error was raised by PlayerDataPuller")



class MatchDataPuller(AbstractDataPuller):
    #concrete game puller class that pulls data for matches
    def __init__(self,api_key,region):
        super().__init__(api_key,region)
    def getMatchInfoByMatchID(self,matchID: int):
        try:
            return self.lol_watcher.match.by_id(self.region,matchID)
        except ApiError as err:
            ApiErrorMessage(err)
    
    def getMatchListByAccountID(self,accountID):
        try:
            return self.lol_watcher.match.matchlist_by_account(self.region,accountID)
        except ApiError as err:
            ApiErrorMessage(err)

    def ApiErrorMessage(self,err):
        super().ApiErrorMessage(err)
        print("This error was raised by MatchDataPuller")

        

    