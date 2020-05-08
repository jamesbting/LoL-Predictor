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
        pass

class PlayerDataPuller(AbstractDataPuller):
    #concretesub class of abstract data puller,
    #pulls player data with various methods, such as account ID, player ID, summoner name, and summoner ID
    def __init__(self,api_key,region):
        super().__init__(api_key,region)
        
    def getPlayerInfoByAccountID(self,accountID):
        try:
            return self.lol_watcher.summoner.by_account(self.region,accountID)
        except ApiError as err:
            ApiErrorMessage(err,accountID)

    def getPlayerInfoBySummonerID(self,summonerID):
        try:
            return self.lol_watcher.summoner.by_account(self.region,summonerID)
        except ApiError as err:
            ApiErrorMessage(err,summonerID)

    def getPlayerInfoBySummonerName(self,summonerName):
        try:
            return self.lol_watcher.summoner.by_name(self.region,summonerName)
        except ApiError as err:
            ApiErrorMessage(err,summonerName)

    def getPlayerInfoByPlayerID(self,playerID):
        try:
            return self.lol_watcher.summoner.by_puuid(self.region,playerID)
            self.lol_watcher.summoner.by_id
        except ApiError as err:
            ApiErrorMessage(err,playerID)

    def ApiErrorMessage(self,err,summonerInfo):
        if err.response.status_code == 429:
            print(f"We should retry in{err.headers['Retry-After']} seconds")
            print("This retry-after is handled by default by the RiotWatcher library")
            print("Future requests must wait until the retry-after time has passed")
        elif err.response.status_code == 404:
            print(f"Summoner with the summoner name/ID: {summonerInfo} could not be found")
        else:
            raise


class MatchDataPuller(AbstractDataPuller):
    #concrete game puller class that pulls data for matches
    def __init__(self,api_key,region):
        super().__init__(api_key,region)
    def ApiErrorMessage(self, err,matchID):
        if err.response.status_code == 429:
            print(f"We should retry in{err.headers['Retry-After']} seconds")
            print("This retry-after is handled by default by the RiotWatcher library")
            print("Future requests must wait until the retry-after time has passed")
        elif err.response.status_code == 404:
            print(f"Match with the match ID: {matchID} could not be found")
        else:
            raise

    