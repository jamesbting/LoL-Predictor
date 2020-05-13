from DataPuller import PlayerDataPuller, MatchDataPuller,ChampionMasteryDataPuller
import csv
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

   
   
    def __init__(self,api_key_location,region,training_data_location):
        self.api_key_location = api_key_location
        f = open(self.api_key_location)
        self.api_key = f.readline()
        f.close()
        self.region = 'na1'
        self.training_data_location = training_data_location

        #the columns are intialized like this to prevent needing to write out each column manually
        for team in DataSetMaker.teams:
            for team_stat in DataSetMaker.team_stats:
                DataSetMaker.columns.append(team + team_stat)

        for summoner in DataSetMaker.summoners:
            for information in DataSetMaker.summoner_information:
                DataSetMaker.columns.append(summoner + information)

            for timeline_information in DataSetMaker.summoner_timeline:
                DataSetMaker.columns.append(summoner + timeline_information)

            for summoner_mastery_information in DataSetMaker.summoner_mastery:
                DataSetMaker.columns.append(summoner+ summoner_mastery_information)

            for information in DataSetMaker.participant_information:
                DataSetMaker.columns.append(summoner + information)

            for stat in DataSetMaker.participant_stats:
                DataSetMaker.columns.append(summoner + stat)
            
        DataSetMaker.columns.append('b_win')
        DataSetMaker.columns.append('r_win')   

             
        
    #function that will make all the rows of the training data
    def makeTrainingData(self):
        player_puller = PlayerDataPuller(self.api_key,self.region)
        match_puller = MatchDataPuller(self.api_key,self.region)
        champion_puller = ChampionMasteryDataPuller(self.api_key,self.region)
        f = open(training_data_location)
        
        f.close()
    
    #function that will write a single match to a file
    def writeMatchToFile(self,matchID,match_puller,file):
        match_data = match_puller.getMatchInfoByMatchID(matchID)
        if match_data['gameMode'] !="CLASSIC" or match_data['mapId'] != 11:
            return

        new_line = []
        #with open(file, newline='') as csvfile:
            #writer = csv.writer(csvfile, delimiter=',', quotechar='"')
            #for set_of_team_stats in [blue_team_stats, red_team_stats]:
        new_line.append(match_data['gameId'])
               
        #add team stats to the row
        new_line = new_line + self.__getTeamStats(match_data)

        new_line = new_line + self.__getSummonerInformation(match_data)
        
        #add victory data
        blue_team_win = match_data["teams"][0]["win"]
        if(blue_team_win):
            new_line.append(1)
            new_line.append(0)
        else: 
            new_line.append(0)
            new_line.append(1)

        print(len(new_line))

    #method that adds the team stats for both teams to a list, then returns the list
    def __getTeamStats(self,match_data):
        team_stats = []
        for teamIndex in [0,1]:
            for team_stat in DataSetMaker.team_stats:
                team_stats.append(match_data['teams'][teamIndex][team_stat])
        return team_stats
    
    #method that adds the summoner information to a list, then returns the list
    def __getSummonerInformation(self, match_data):
        summonerInformation = []
        player_puller = PlayerDataPuller(self.api_key,self.region)
        champion_mastery_puller = ChampionMasteryDataPuller(self.api_key,self.region)

        for participantIdentitiesIndex in range(0,10):
            participantInformation = self.__getParticipantInformation(match_data,participantIdentitiesIndex,player_puller,champion_mastery_puller)
            summonerInformation = summonerInformation + participantInformation

            participantStats = self.__getParticipantStats(match_data,participantIdentitiesIndex)
            summonerInformation = summonerInformation + participantStats
            
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
        player_data = player_puller.getPlayerInfoByAccountID(accountID=accountId)
        summonerLevel = player_data["summonerLevel"]

        role =  match_data["participants"][index]["timeline"]["role"]
        lane =  match_data["participants"][index]["timeline"]["lane"]
        
        #append the data to the list
        participantInformation.append(accountId)
        participantInformation.append(summonerLevel)
        participantInformation.append(role)
        participantInformation.append(lane)

        #get champion mastery information
        participantInformation = participantInformation + self.__getParticipantChampionMastery(match_data,index,champion_mastery_puller)

        championId = match_data["participants"][index]["championId"]
        spell1Id = match_data["participants"][index]["spell1Id"]
        spell2Id = match_data["participants"][index]["spell2Id"]

        participantInformation.append(championId)
        participantInformation.append(spell1Id)
        participantInformation.append(spell2Id)

        return participantInformation
        
    #get champion mastery information
    def __getParticipantChampionMastery(self,match_data,index,champion_mastery_puller):
        participant_mastery_information = []
        summonerId = match_data["participantIdentities"][index]["player"]["summonerId"]
        championId = match_data["participants"][index]["championId"]

        champion_mastery_information = champion_mastery_puller.getChampionMastery(summonerId,championId)
        for mastery_information in DataSetMaker.summoner_mastery:
            if(mastery_information != 'totalChampionMastery'):
                participant_mastery_information.append(champion_mastery_information[mastery_information])
        
        total_mastery = champion_mastery_puller.getTotalChampionMastery(summonerId)
        participant_mastery_information.append(total_mastery)
        
        return participant_mastery_information
    
    #get the stats for a participant for this game
    def __getParticipantStats(self,match_data,index):
        participantStats = []
        for stat in DataSetMaker.participant_stats:
            participantStats.append(match_data["participants"][index]["stats"][stat])

        return participantStats

        
def main():
    region = 'na1'
    f = open("api_key.txt","r")
    api_key = f.readline()
    f.close()
    match_puller = MatchDataPuller(api_key,region)
    data_set_maker = DataSetMaker("api_key.txt",region,None)
    data_set_maker.writeMatchToFile(3073903129,match_puller,None)
    print(len(DataSetMaker.columns))

main()



 