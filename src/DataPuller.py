from riotwatcher import LolWatcher,ApiError
import time

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
            print("We should retry in {seconds} seconds".format(seconds = err.headers['Retry-After']))
            print("This retry-after is handled by default by the RiotWatcher library")
            print("Future requests must wait until the retry-after time has passed")
            time.sleep(30)
        elif err.response.status_code == 404:
            print("No such information could not be found")
        elif err.response.status_code == 504:
            time.sleep(30)
        elif err.response.status_code == 503:
            time.sleep(30)

class PlayerDataPuller(AbstractDataPuller):
    #concrete subclass of abstract data puller,
    #pulls player data with various methods, such as account ID, player ID, summoner name, and summoner ID
    def __init__(self,api_key,region):
        super().__init__(api_key,region)
        
    def getPlayerInfoByAccountID(self,accountID):
        try:
            return self.lol_watcher.summoner.by_account(self.region,accountID)
        except ApiError as err:
           self.ApiErrorMessage(err)

    def getPlayerInfoBySummonerID(self,summonerID):
        try:
            return self.lol_watcher.summoner.by_account(self.region,summonerID)
        except ApiError as err:
           self.ApiErrorMessage(err)

    def getPlayerInfoBySummonerName(self,summonerName):
        try:
            return self.lol_watcher.summoner.by_name(self.region,summonerName)
        except ApiError as err:
           self.ApiErrorMessage(err)

    def getPlayerInfoByPlayerID(self,playerID):
        try:
            return self.lol_watcher.summoner.by_puuid(self.region,playerID)
            self.lol_watcher.summoner.by_id
        except ApiError as err:
           self.ApiErrorMessage(err)

    def ApiErrorMessage(self,err):
        super().ApiErrorMessage(err)
        print("This error was raised by ",type(self).__name__)


class MatchDataPuller(AbstractDataPuller):
    #concrete game puller class that pulls data for matches
    def __init__(self,api_key,region):
        super().__init__(api_key,region)
    def getMatchInfoByMatchID(self,matchID):
        try:
            return self.lol_watcher.match.by_id(self.region,matchID)
        except ApiError as err:
           self.ApiErrorMessage(err)
    
    def getMatchListByAccountID(self,accountID,queue = None,season = None):
        try:
            return self.lol_watcher.match.matchlist_by_account(self.region,accountID,queue,season)
        except ApiError as err:
           self.ApiErrorMessage(err)

    def ApiErrorMessage(self,err):
        super().ApiErrorMessage(err)
        print("This error was raised by ",type(self).__name__)

class ChampionMasteryDataPuller(AbstractDataPuller):
    def __init__(self,api_key,region):
        super().__init__(api_key,region)

    def getChampionMastery(self,summonerID,championID):
        try:
            return self.lol_watcher.champion_mastery.by_summoner_by_champion(self.region,summonerID,championID)
        except ApiError as err:
           self.ApiErrorMessage(err)
    
    def getTotalChampionMastery(self,summonerID):
        try:
            return self.lol_watcher.champion_mastery.scores_by_summoner(self.region,summonerID)
        except ApiError as err:
           self.ApiErrorMessage(err)

    def ApiErrorMessage(self,err):
        super().ApiErrorMessage(err)
        print("This error was raised by ",type(self).__name__)

    