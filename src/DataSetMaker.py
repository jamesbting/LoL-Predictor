from DataPuller import PlayerDataPuller, MatchDataPuller,ChampionMasteryDataPuller
import csv
from SummonerCrawler import SummonerCrawler
from tqdm import tqdm
import time
class DataSetMaker:
    #match id, then team stats then individual summoner stats(blue team, then red team), lastly which team won
    columns = ['gameId']
                #team stats
    team_stats =['firstBlood','firstTower','firstInhibitor','firstBaron','firstDragon','firstRiftHerald',
                 'towerKills','inhibitorKills','baronKills','dragonKills','riftHeraldKills']
    teams = ["b_","r_"]
    summoners = ['b_summoner1_','b_summoner2_','b_summoner3_','b_summoner4_','b_summoner5_',
                'r_summoner1_','r_summoner2_','r_summoner3_','r_summoner4_','r_summoner5_']
    
    summoner_information = ["accountId",'level']
    summoner_timeline = ['role','lane',]
    summoner_mastery = ['championLevel','championPoints','lastPlayTime','championPointsSinceLastLevel','championPointsUntilNextLevel','chestGranted','tokensEarned','totalChampionMastery']
    participant_information = ['championId','spell1Id','spell2Id']
    participant_stats = [
                     'item0','item1','item2','item3','item4','item5','item6','kills','deaths','assists','largestKillingSpree','largestMultiKill','killingSprees',
                     'longestTimeSpentLiving','doubleKills','tripleKills','quadraKills','pentaKills','totalDamageDealt','magicDamageDealt','physicalDamageDealt',
                     'trueDamageDealt','largestCriticalStrike','totalDamageDealtToChampions','magicDamageDealtToChampions','physicalDamageDealtToChampions',
                     'trueDamageDealtToChampions','totalHeal', 'totalUnitsHealed','damageSelfMitigated','damageDealtToObjectives','damageDealtToTurrets',
                     'visionScore','timeCCingOthers','totalDamageTaken','magicalDamageTaken','physicalDamageTaken','trueDamageTaken','goldEarned','goldSpent',
                     'turretKills','inhibitorKills','totalMinionsKilled','neutralMinionsKilled','neutralMinionsKilledTeamJungle','neutralMinionsKilledEnemyJungle',
                     'totalTimeCrowdControlDealt','champLevel','visionWardsBoughtInGame','sightWardsBoughtInGame','wardsPlaced', 'wardsKilled', 'firstBloodKill',
                     'firstBloodAssist','firstTowerKill','firstTowerAssist','combatPlayerScore','objectivePlayerScore','totalPlayerScore', 'totalScoreRank']

   
   
    def __init__(self,api_key_location,region,training_data_location,starting_matchID,num_data_points = 10000):
        self.api_key_location = api_key_location
        f = open(self.api_key_location)
        self.api_key = f.readline()
        f.close()
        self.region = 'na1'
        self.training_data_location = training_data_location
        self.starting_matchID = starting_matchID
        self.num_data_points = num_data_points
        #add all the match Id's to the set that are in the training data file already
        self.added_matches = set()
        

        with open(self.training_data_location,"r") as f:
            for row in f:
                self.added_matches.add(row[0])

        #the columns are initialized like this to prevent needing to write out each column manually
        append = DataSetMaker.columns.append
        for team in DataSetMaker.teams:
            for team_stat in DataSetMaker.team_stats:
               append("%s%s" % (team,team_stat))

        for summoner in DataSetMaker.summoners:
            for information in DataSetMaker.summoner_information:
                append("%s%s" % (summoner,information))

            for timeline_information in DataSetMaker.summoner_timeline:
                append("%s%s" % (summoner,timeline_information))

            for summoner_mastery_information in DataSetMaker.summoner_mastery:
                append("%s%s" % (summoner,summoner_mastery_information))

            for information in DataSetMaker.participant_information:
                append("%s%s" % (summoner,information))

            for stat in DataSetMaker.participant_stats:
                append("%s%s" % (summoner,stat))
            
        DataSetMaker.columns.append('b_win')
        DataSetMaker.columns.append('r_win')   

        self.firstTower = False #since the riot API skips the firstTowerKill and firstTowerAssist for participant stats if no tower is destroyed
        
    #function that will make all the rows of the training data
    def makeTrainingData(self):
        match_puller = MatchDataPuller(self.api_key,self.region)
        crawler = SummonerCrawler(self.api_key,self.region,self.starting_matchID,self.num_data_points)
        matchID = self.starting_matchID
        pbar = tqdm(total = self.num_data_points)

        #local variables to speed up processing, and void using the "." operator
        writeMatch = self.writeMatchToFile
        hasNext = crawler.hasNext
        nextID = crawler.next

        while(hasNext()):
            if(matchID not in self.added_matches):
                try:
                    writeMatch(matchID,match_puller,self.training_data_location)
                except:
                    #something went wrong, just skip this match
                    matchID = nextID(worked = False)
                    continue

            matchID = nextID()
            pbar.update(1)
        
        #done looping
        pbar.close()
        
    #function that will write a single match to a file
    def writeMatchToFile(self,matchID,match_puller,filename):
        newLine = self.__newMatchLine(matchID,match_puller)
        with open(filename,'a',newline = '\n') as f:
                writer = csv.writer(f)
                writer.writerow(newLine)
        f.close()
        self.added_matches.add(newLine[0])

        

    def __newMatchLine(self,matchID,match_puller):
        match_data = match_puller.getMatchInfoByMatchID(matchID)
        #if match_data['gameMode'] !="CLASSIC" or match_data['mapId'] != 11: #only get classic game mode from Summoner's Rift
            #return

        new_line = []
        new_line.append(match_data['gameId'])
        #add team stats to the row
        new_line.extend(self.__getTeamStats(match_data))

        #add summoner stats to the row
        new_line.extend(self.__getSummonerInformation(match_data))
        
        #add victory data
        blue_team_win = match_data["teams"][0]["win"]
        if(blue_team_win == "Win"):
            new_line.extend([1,0])
        else: 
            new_line.extend([0,1])

        return new_line
    #method that adds the team stats for both teams to a list, then returns the list
    def __getTeamStats(self,match_data):
        team_stats = []
        first_tower = [False,False]
        append = team_stats.append
        for teamIndex in [0,1]:
            for team_stat in DataSetMaker.team_stats:
                if(team_stat == "firstTower"):
                    new_stat = match_data['teams'][teamIndex][team_stat]
                    append(new_stat)
                    first_tower[teamIndex] = new_stat
                else:
                   append(match_data['teams'][teamIndex][team_stat])

        self.firstTower = first_tower[0] or first_tower[1]
        return team_stats
    
    #method that adds all the summoner information to a list, then returns the list
    def __getSummonerInformation(self, match_data):
        summonerInformation = []
        player_puller = PlayerDataPuller(self.api_key,self.region)
        champion_mastery_puller = ChampionMasteryDataPuller(self.api_key,self.region)

        extend = summonerInformation.extend
        getParticipantInformation = self.__getParticipantInformation
        getParticipantStats = self.__getParticipantStats
        for participantIdentitiesIndex in range(0,10):
            #get summoner information
            
            extend(getParticipantInformation(match_data,participantIdentitiesIndex,player_puller,champion_mastery_puller))

            #get summoner stats
            extend(getParticipantStats(match_data,participantIdentitiesIndex))
            
        return summonerInformation

    #gets all the other information other than summoner stats in the same order as the columns
    #for reference:
    #summoner_information = ["accountId",'level']
    #summoner_timeline = ['role','lane',]
    #summoner_mastery = ['championLevel','championPoints','lastPlayTime','championPointsSinceLastLevel','championPointsUntilNextLevel','chestGranted',
    #                   'tokensEarned','totalChampionMastery']
    #participant_information = ['championId','spell1Id','spell2Id']
    def __getParticipantInformation(self,match_data,index,player_puller,champion_mastery_puller):
        participantInformation = []
        accountId = match_data["participantIdentities"][index]["player"]["accountId"]
        
        #get summoner level based on account id
        player_data = player_puller.getPlayerInfoByAccountID(accountId)
        
        #append the data to the list
        participantInformation.extend([accountId,player_data["summonerLevel"],match_data["participants"][index]["timeline"]["role"],
                                       match_data["participants"][index]["timeline"]["lane"]])

        #get champion mastery information
        participantInformation.extend(self.__getParticipantChampionMastery(match_data,index,champion_mastery_puller))

    
        #add participant Information to list
        participantInformation.extend([match_data["participants"][index]["championId"],match_data["participants"][index]["spell1Id"],
                                       match_data["participants"][index]["spell2Id"]])

        return participantInformation
        
    #get champion mastery information
    def __getParticipantChampionMastery(self,match_data,index,champion_mastery_puller):
        participant_mastery_information = [] # return value

        #get necessary IDs
        summonerId = match_data["participantIdentities"][index]["player"]["summonerId"]
        championId = match_data["participants"][index]["championId"]

        #get mastery information and add to list
        champion_mastery_information = champion_mastery_puller.getChampionMastery(summonerId,championId)
        append = participant_mastery_information.append
        for mastery_information in DataSetMaker.summoner_mastery[:-1]:
               append(champion_mastery_information[mastery_information])
        
        #add total mastery information to list
        total_mastery = champion_mastery_puller.getTotalChampionMastery(summonerId)
        append(total_mastery)
        
        return participant_mastery_information
    
    #get the stats for a participant for this game
    #check the first tower adding to stat list problem
    def __getParticipantStats(self,match_data,index):
        participantStats = []
        append = participantStats.append
        for stat in DataSetMaker.participant_stats:
            if(stat == 'firstTowerKill' or stat == 'firstTowerAssist'):
                if self.firstTower:
                    append(match_data["participants"][index]["stats"][stat])
                else:
                    #no one got first tower, so add false for firstTower kill and assist to all participants
                    append("False")
            else:
                append(match_data["participants"][index]["stats"][stat])

        return participantStats




 