#returns the indexes of all excluded columns

excluded_columns = ["accountId",'role','lane','lastPlayTime']

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

def make_columns():
    columns = ['gameId']
    append = columns.append
    for team in teams:
        for team_stat in team_stats:
            append("%s%s" % (team,team_stat))

    for summoner in summoners:
        for information in summoner_information:
            append("%s%s" % (summoner,information))

        for timeline_information in summoner_timeline:
            append("%s%s" % (summoner,timeline_information))

        for summoner_mastery_information in summoner_mastery:
            append("%s%s" % (summoner,summoner_mastery_information))

        for information in participant_information:
            append("%s%s" % (summoner,information))

        for stat in participant_stats:
            append("%s%s" % (summoner,stat))
        
    append('b_win')
    append('r_win')   
    return columns
def make_excluded_columns():
    excluded_columns_with_summoner = []
    for summoner in summoners:
         excluded_columns_with_summoner.extend(["%s%s" % (summoner,excluded_column) for excluded_column in excluded_columns])
    return excluded_columns_with_summoner


columns = make_columns()
excluded_columns_with_summoner = make_excluded_columns()
final = [0]
final.extend([columns.index(excluded_column) for excluded_column in excluded_columns_with_summoner])
print(final)