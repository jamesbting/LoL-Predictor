import csv
#returns the indexes of all excluded columns that are to be excluded from the data set. for use before training a model to only pass the data
class ExcludeColumnsGenerator():
    columns = ['gameId']
                    #team stats
    team_stats =['firstBlood','firstTower','firstInhibitor','firstBaron','firstDragon','firstRiftHerald',
                    'towerKills','inhibitorKills','baronKills','dragonKills','riftHeraldKills']
    teams = ["b_","r_"]
    summoners = ['b_summoner1_','b_summoner2_','b_summoner3_','b_summoner4_','b_summoner5_',
                'r_summoner1_','r_summoner2_','r_summoner3_','r_summoner4_','r_summoner5_']

    summoner_information = ["accountId",'level','role','lane','championLevel','championPoints','lastPlayTime','championPointsSinceLastLevel','championPointsUntilNextLevel','chestGranted','tokensEarned','totalChampionMastery',
                        'championId','spell1Id','spell2Id','item0','item1','item2','item3','item4','item5','item6','kills','deaths','assists','largestKillingSpree','largestMultiKill','killingSprees',
                        'longestTimeSpentLiving','doubleKills','tripleKills','quadraKills','pentaKills','totalDamageDealt','magicDamageDealt','physicalDamageDealt',
                        'trueDamageDealt','largestCriticalStrike','totalDamageDealtToChampions','magicDamageDealtToChampions','physicalDamageDealtToChampions',
                        'trueDamageDealtToChampions','totalHeal', 'totalUnitsHealed','damageSelfMitigated','damageDealtToObjectives','damageDealtToTurrets',
                        'visionScore','timeCCingOthers','totalDamageTaken','magicalDamageTaken','physicalDamageTaken','trueDamageTaken','goldEarned','goldSpent',
                        'turretKills','inhibitorKills','totalMinionsKilled','neutralMinionsKilled','neutralMinionsKilledTeamJungle','neutralMinionsKilledEnemyJungle',
                        'totalTimeCrowdControlDealt','champLevel','visionWardsBoughtInGame','sightWardsBoughtInGame','wardsPlaced', 'wardsKilled', 'firstBloodKill',
                        'firstBloodAssist','firstTowerKill','firstTowerAssist','combatPlayerScore','objectivePlayerScore','totalPlayerScore', 'totalScoreRank']


    def __init__(self, pre_match,include_gameID = False):
        self.pre_match = pre_match #set to true if you want to exclude the post match data
        self.include_gameID = include_gameID
        
        
        if self.pre_match:
            self.excluded_team_columns = ['firstBlood','firstTower','firstInhibitor','firstBaron','firstDragon','firstRiftHerald','towerKills','inhibitorKills','baronKills','dragonKills','riftHeraldKills']
            self.excluded_summoner_columns = ["accountId",'role','lane','lastPlayTime','item0','item1','item2','item3','item4','item5','item6','kills','deaths','assists','largestKillingSpree','largestMultiKill','killingSprees',
                            'longestTimeSpentLiving','doubleKills','tripleKills','quadraKills','pentaKills','totalDamageDealt','magicDamageDealt','physicalDamageDealt',
                            'trueDamageDealt','largestCriticalStrike','totalDamageDealtToChampions','magicDamageDealtToChampions','physicalDamageDealtToChampions',
                            'trueDamageDealtToChampions','totalHeal', 'totalUnitsHealed','damageSelfMitigated','damageDealtToObjectives','damageDealtToTurrets',
                            'visionScore','timeCCingOthers','totalDamageTaken','magicalDamageTaken','physicalDamageTaken','trueDamageTaken','goldEarned','goldSpent',
                            'turretKills','inhibitorKills','totalMinionsKilled','neutralMinionsKilled','neutralMinionsKilledTeamJungle','neutralMinionsKilledEnemyJungle',
                            'totalTimeCrowdControlDealt','champLevel','visionWardsBoughtInGame','sightWardsBoughtInGame','wardsPlaced', 'wardsKilled', 'firstBloodKill',
                            'firstBloodAssist','firstTowerKill','firstTowerAssist','combatPlayerScore','objectivePlayerScore','totalPlayerScore', 'totalScoreRank']
        else:
            self.excluded_team_columns = []
            self.excluded_summoner_columns = ["accountId",'role','lane','lastPlayTime']

        self.columns = self.__make_columns()


    def __make_columns(self):
        columns = ExcludeColumnsGenerator.columns
        append = self.columns.append
        for team in ExcludeColumnsGenerator.teams:
            for team_stat in ExcludeColumnsGenerator.team_stats:
                append("%s%s" % (team,team_stat))
        for summoner in ExcludeColumnsGenerator.summoners:
            for information in ExcludeColumnsGenerator.summoner_information:
                append("%s%s" % (summoner,information))
        append('b_win')
        append('r_win') 
        return columns

    def __make_excluded_columns(self):
        excluded_columns = []
        for team in ExcludeColumnsGenerator.teams:
            excluded_columns.extend(["%s%s" % (team,excluded_column) for excluded_column in self.excluded_team_columns])
        for summoner in ExcludeColumnsGenerator.summoners:
            excluded_columns.extend(["%s%s" % (summoner,excluded_column) for excluded_column in self.excluded_summoner_columns])
        return excluded_columns


    def excluded_indexes(self):
        excluded_columns = self.__make_excluded_columns()
        final = []
        if (self.include_gameID is False):
            final.append(0) #omit the game ID
        final.extend([self.columns.index(excluded_column) for excluded_column in excluded_columns])
        return final

def main():
    pre_match = True
    include_gameID = False
    generator = ExcludeColumnsGenerator(pre_match, include_gameID)
    exclude = generator.excluded_indexes()
    print(len(exclude))
    if pre_match:
        with open("C:\\Users\\James Ting\\OneDrive - McGill University\\Personal\\Personal Projects\\LoL-Predictor\\docs\\PreMatchExcludedColumns.csv","w") as f:
            writer = csv.writer(f)
            writer.writerow(exclude)
            print("Success!")
    else:
         with open("C:\\Users\\James Ting\\OneDrive - McGill University\\Personal\\Personal Projects\\LoL-Predictor\\docs\\PostMatchExcludedColumns.csv","w") as f:
            writer = csv.writer(f)
            writer.writerow(exclude)
            print("Success!")

main()