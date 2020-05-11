from DataPuller import PlayerDataPuller, MatchDataPuller,ChampionMasteryDataPuller
class DataSetMaker:
    #match id, then team stats then individual summoner stats(blue team, then red team,75 features for each summoner), lastly which team won
    #there must be a better way to do this but I can't think of it at the moment
    columns = ['matchId',
                #team stats
               'b_tower_kills','b_rift_herald_kills','b_first_blood','b_inhibitor_kills','b_first_baron','b_first_dragon','b_dragon_kills','b_baron_kills','b_first_inhibitor','b_first_tower','b_first_rift_herald',
               'r_tower_kills','r_rift_herald_kills','r_first_blood','r_inhibitor_kills','r_first_baron','r_first_dragon','r_dragon_kills','r_baron_kills','r_first_inhibitor','r_first_tower','r_first_rift_herald',
               
               #blue team summoner 1 stats
               'b_summoner1_accountID','b_summoner1_position','b_summoner1_level','b_summoner1_champion','b_summoner1_champion_mastery','b_summoner1_champion_mastery','b_summoner1_champion_points_until_next_level',
               'b_summoner1_chest_granted','b_summoner1_champion_last_play_time','b_summoner1_champion_level','b_summoner1_champion_points_since_last_level','b_summoner1_tokens_earned','b_summoner1_total_mastery',
               'b_summoner1_item0','b_summoner1_item1','b_summoner1_item2','b_summoner1_item3','b_summoner1_item4','b_summoner1_item5','b_summoner1_item6','b_summoner1_totalUnitsHealed','b_summoner1_largestMultiKill',
               'b_summoner1_goldEarned','b_summoner1_firstInhibitorKill','b_summoner1_physicalDamageTaken','b_summoner1_totalPlayerScore','b_summoner1_championLevel','b_summoner1_damageDealtToObjectives','b_summoner1_totalDamageTaken',
               'b_summoner1_neturalMinionsKilled','b_summoner1_deaths','b_summoner1_tripleKills','b_summoner1_magicDamageDealtToChampions','b_summoner1_wardsKilled','b_summoner1_pentaKills','b_summoner1_damageSelfMitigated',
               'b_summoner1_largestCriticalStrike','b_summoner1_totalTimeCrowdControlDealt','b_summoner1_firstTowerKill','b_summoner1_magicDamageDealt','b_summoner1_totalScoreRank','b_summoner1_wardsPlaced','b_summoner1_totalDamageDealt',
               'b_summoner1_timeCCingOthers','b_summoner1_magicalDamageTaken','b_summoner1_largestKillingSpree','b_summoner1_totalDamageDealtToChampions','b_summoner1_physicalDamageDealtToChampions',
               'b_summoner1_neturalMinionsKilledTeamJungle','b_summoner1_totalMinionsKilled','b_summoner1_firstInhibitorAssist','b_summoner1_visionWardsBought','b_summoner1_objectivePlayerScore',
               'b_summoner1_kills','b_summoner1_firstTowerAssist','b_summoner1_combatPlayerScore','b_summoner1_inhibitorKills','b_summoner1_turretKills','b_summoner1_trueDamageTaken','b_summoner1_firstBloodAssist',
               'b_summoner1_assits','b_summoner1_goldSpent','b_summoner1_damageDealtToTurrets','b_summoner1_total_heal','b_summoner1_visionScore','b_summoner1_physicalDamageDealt','b_summoner1_firstBloodKill',
               'b_summoner1_longestTimeSpentLiving','b_summoner1_killingSprees','b_summoner1_trueDamageDealtToChampions','b_summoner1_doubleKills','b_summoner1_trueDamageDealth','b_summoner1_quadraKills',
               'b_summoner1_spell1','b_summoner1_spell2',
               
                #blue team summoner 2 stats
               'b_summoner2_accountID','b_summoner2_position','b_summoner2_level','b_summoner2_champion','b_summoner2_champion_mastery','b_summoner2_champion_mastery','b_summoner2_champion_points_until_next_level',
               'b_summoner2_chest_granted','b_summoner2_champion_last_play_time','b_summoner2_champion_level','b_summoner2_champion_points_since_last_level','b_summoner2_tokens_earned','b_summoner2_total_mastery',
               'b_summoner2_item0','b_summoner2_item1','b_summoner2_item2','b_summoner2_item3','b_summoner2_item4','b_summoner2_item5','b_summoner2_item6','b_summoner2_totalUnitsHealed','b_summoner2_largestMultiKill',
               'b_summoner2_goldEarned','b_summoner2_firstInhibitorKill','b_summoner2_physicalDamageTaken','b_summoner2_totalPlayerScore','b_summoner2_championLevel','b_summoner2_damageDealtToObjectives','b_summoner2_totalDamageTaken',
               'b_summoner2_neturalMinionsKilled','b_summoner2_deaths','b_summoner2_tripleKills','b_summoner2_magicDamageDealtToChampions','b_summoner2_wardsKilled','b_summoner2_pentaKills','b_summoner2_damageSelfMitigated',
               'b_summoner2_largestCriticalStrike','b_summoner2_totalTimeCrowdControlDealt','b_summoner2_firstTowerKill','b_summoner2_magicDamageDealt','b_summoner2_totalScoreRank','b_summoner2_wardsPlaced','b_summoner2_totalDamageDealt',
               'b_summoner2_timeCCingOthers','b_summoner2_magicalDamageTaken','b_summoner2_largestKillingSpree','b_summoner2_totalDamageDealtToChampions','b_summoner2_physicalDamageDealtToChampions',
               'b_summoner2_neturalMinionsKilledTeamJungle','b_summoner2_totalMinionsKilled','b_summoner2_firstInhibitorAssist','b_summoner2_visionWardsBought','b_summoner2_objectivePlayerScore',
               'b_summoner2_kills','b_summoner2_firstTowerAssist','b_summoner2_combatPlayerScore','b_summoner2_inhibitorKills','b_summoner2_turretKills','b_summoner2_trueDamageTaken','b_summoner2_firstBloodAssist',
               'b_summoner2_assits','b_summoner2_goldSpent','b_summoner2_damageDealtToTurrets','b_summoner2_total_heal','b_summoner2_visionScore','b_summoner2_physicalDamageDealt','b_summoner2_firstBloodKill',
               'b_summoner2_longestTimeSpentLiving','b_summoner2_killingSprees','b_summoner2_trueDamageDealtToChampions','b_summoner2_doubleKills','b_summoner2_trueDamageDealth','b_summoner2_quadraKills',
               'b_summoner2_spell1','b_summoner2_spell2',

               #blue team summoner 3 stats
               'b_summoner3_accountID','b_summoner3_position','b_summoner3_level','b_summoner3_champion','b_summoner3_champion_mastery','b_summoner3_champion_mastery','b_summoner3_champion_points_until_next_level',
               'b_summoner3_chest_granted','b_summoner3_champion_last_play_time','b_summoner3_champion_level','b_summoner3_champion_points_since_last_level','b_summoner3_tokens_earned','b_summoner3_total_mastery',
               'b_summoner3_item0','b_summoner3_item1','b_summoner3_item2','b_summoner3_item3','b_summoner3_item4','b_summoner3_item5','b_summoner3_item6','b_summoner3_totalUnitsHealed','b_summoner3_largestMultiKill',
               'b_summoner3_goldEarned','b_summoner3_firstInhibitorKill','b_summoner3_physicalDamageTaken','b_summoner3_totalPlayerScore','b_summoner3_championLevel','b_summoner3_damageDealtToObjectives','b_summoner3_totalDamageTaken',
               'b_summoner3_neturalMinionsKilled','b_summoner3_deaths','b_summoner3_tripleKills','b_summoner3_magicDamageDealtToChampions','b_summoner3_wardsKilled','b_summoner3_pentaKills','b_summoner3_damageSelfMitigated',
               'b_summoner3_largestCriticalStrike','b_summoner3_totalTimeCrowdControlDealt','b_summoner3_firstTowerKill','b_summoner3_magicDamageDealt','b_summoner3_totalScoreRank','b_summoner3_wardsPlaced','b_summoner3_totalDamageDealt',
               'b_summoner3_timeCCingOthers','b_summoner3_magicalDamageTaken','b_summoner3_largestKillingSpree','b_summoner3_totalDamageDealtToChampions','b_summoner3_physicalDamageDealtToChampions',
               'b_summoner3_neturalMinionsKilledTeamJungle','b_summoner3_totalMinionsKilled','b_summoner3_firstInhibitorAssist','b_summoner3_visionWardsBought','b_summoner3_objectivePlayerScore',
               'b_summoner3_kills','b_summoner3_firstTowerAssist','b_summoner3_combatPlayerScore','b_summoner3_inhibitorKills','b_summoner3_turretKills','b_summoner3_trueDamageTaken','b_summoner3_firstBloodAssist',
               'b_summoner3_assits','b_summoner3_goldSpent','b_summoner3_damageDealtToTurrets','b_summoner3_total_heal','b_summoner3_visionScore','b_summoner3_physicalDamageDealt','b_summoner3_firstBloodKill',
               'b_summoner3_longestTimeSpentLiving','b_summoner3_killingSprees','b_summoner3_trueDamageDealtToChampions','b_summoner3_doubleKills','b_summoner3_trueDamageDealth','b_summoner3_quadraKills',
               'b_summoner3_spell1','b_summoner3_spell2',

               #blue team summoner 4 stats
               'b_summoner4_accountID','b_summoner4_position','b_summoner4_level','b_summoner4_champion','b_summoner4_champion_mastery','b_summoner4_champion_mastery','b_summoner4_champion_points_until_next_level',
               'b_summoner4_chest_granted','b_summoner4_champion_last_play_time','b_summoner4_champion_level','b_summoner4_champion_points_since_last_level','b_summoner4_tokens_earned','b_summoner4_total_mastery',
               'b_summoner4_item0','b_summoner4_item1','b_summoner4_item2','b_summoner4_item3','b_summoner4_item4','b_summoner4_item5','b_summoner4_item6','b_summoner4_totalUnitsHealed','b_summoner4_largestMultiKill',
               'b_summoner4_goldEarned','b_summoner4_firstInhibitorKill','b_summoner4_physicalDamageTaken','b_summoner4_totalPlayerScore','b_summoner4_championLevel','b_summoner4_damageDealtToObjectives','b_summoner4_totalDamageTaken',
               'b_summoner4_neturalMinionsKilled','b_summoner4_deaths','b_summoner4_tripleKills','b_summoner4_magicDamageDealtToChampions','b_summoner4_wardsKilled','b_summoner4_pentaKills','b_summoner4_damageSelfMitigated',
               'b_summoner4_largestCriticalStrike','b_summoner4_totalTimeCrowdControlDealt','b_summoner4_firstTowerKill','b_summoner4_magicDamageDealt','b_summoner4_totalScoreRank','b_summoner4_wardsPlaced','b_summoner4_totalDamageDealt',
               'b_summoner4_timeCCingOthers','b_summoner4_magicalDamageTaken','b_summoner4_largestKillingSpree','b_summoner4_totalDamageDealtToChampions','b_summoner4_physicalDamageDealtToChampions',
               'b_summoner4_neturalMinionsKilledTeamJungle','b_summoner4_totalMinionsKilled','b_summoner4_firstInhibitorAssist','b_summoner4_visionWardsBought','b_summoner4_objectivePlayerScore',
               'b_summoner4_kills','b_summoner4_firstTowerAssist','b_summoner4_combatPlayerScore','b_summoner4_inhibitorKills','b_summoner4_turretKills','b_summoner4_trueDamageTaken','b_summoner4_firstBloodAssist',
               'b_summoner4_assits','b_summoner4_goldSpent','b_summoner4_damageDealtToTurrets','b_summoner4_total_heal','b_summoner4_visionScore','b_summoner4_physicalDamageDealt','b_summoner4_firstBloodKill',
               'b_summoner4_longestTimeSpentLiving','b_summoner4_killingSprees','b_summoner4_trueDamageDealtToChampions','b_summoner4_doubleKills','b_summoner4_trueDamageDealth','b_summoner4_quadraKills',
               'b_summoner4_spell1','b_summoner4_spell2',

               #blue team summoner 5 stats
               'b_summoner5_accountID','b_summoner5_position','b_summoner5_level','b_summoner5_champion','b_summoner5_champion_mastery','b_summoner5_champion_mastery','b_summoner5_champion_points_until_next_level',
               'b_summoner5_chest_granted','b_summoner5_champion_last_play_time','b_summoner5_champion_level','b_summoner5_champion_points_since_last_level','b_summoner5_tokens_earned','b_summoner5_total_mastery',
               'b_summoner5_item0','b_summoner5_item1','b_summoner5_item2','b_summoner5_item3','b_summoner5_item4','b_summoner5_item5','b_summoner5_item6','b_summoner5_totalUnitsHealed','b_summoner5_largestMultiKill',
               'b_summoner5_goldEarned','b_summoner5_firstInhibitorKill','b_summoner5_physicalDamageTaken','b_summoner5_totalPlayerScore','b_summoner5_championLevel','b_summoner5_damageDealtToObjectives','b_summoner5_totalDamageTaken',
               'b_summoner5_neturalMinionsKilled','b_summoner5_deaths','b_summoner5_tripleKills','b_summoner5_magicDamageDealtToChampions','b_summoner5_wardsKilled','b_summoner5_pentaKills','b_summoner5_damageSelfMitigated',
               'b_summoner5_largestCriticalStrike','b_summoner5_totalTimeCrowdControlDealt','b_summoner5_firstTowerKill','b_summoner5_magicDamageDealt','b_summoner5_totalScoreRank','b_summoner5_wardsPlaced','b_summoner5_totalDamageDealt',
               'b_summoner5_timeCCingOthers','b_summoner5_magicalDamageTaken','b_summoner5_largestKillingSpree','b_summoner5_totalDamageDealtToChampions','b_summoner5_physicalDamageDealtToChampions',
               'b_summoner5_neturalMinionsKilledTeamJungle','b_summoner5_totalMinionsKilled','b_summoner5_firstInhibitorAssist','b_summoner5_visionWardsBought','b_summoner5_objectivePlayerScore',
               'b_summoner5_kills','b_summoner5_firstTowerAssist','b_summoner5_combatPlayerScore','b_summoner5_inhibitorKills','b_summoner5_turretKills','b_summoner5_trueDamageTaken','b_summoner5_firstBloodAssist',
               'b_summoner5_assits','b_summoner5_goldSpent','b_summoner5_damageDealtToTurrets','b_summoner5_total_heal','b_summoner5_visionScore','b_summoner5_physicalDamageDealt','b_summoner5_firstBloodKill',
               'b_summoner5_longestTimeSpentLiving','b_summoner5_killingSprees','b_summoner5_trueDamageDealtToChampions','b_summoner5_doubleKills','b_summoner5_trueDamageDealth','b_summoner5_quadraKills',
               'b_summoner5_spell1','b_summoner5_spell2',

               #red team summoner 1 stats
               'r_summoner1_accountID','r_summoner1_position','r_summoner1_level','r_summoner1_champion','r_summoner1_champion_mastery','r_summoner1_champion_mastery','r_summoner1_champion_points_until_next_level',
               'r_summoner1_chest_granted','r_summoner1_champion_last_play_time','r_summoner1_champion_level','r_summoner1_champion_points_since_last_level','r_summoner1_tokens_earned','r_summoner1_total_mastery',
               'r_summoner1_item0','r_summoner1_item1','r_summoner1_item2','r_summoner1_item3','r_summoner1_item4','r_summoner1_item5','r_summoner1_item6','r_summoner1_totalUnitsHealed','r_summoner1_largestMultiKill',
               'r_summoner1_goldEarned','r_summoner1_firstInhibitorKill','r_summoner1_physicalDamageTaken','r_summoner1_totalPlayerScore','r_summoner1_championLevel','r_summoner1_damageDealtToObjectives','r_summoner1_totalDamageTaken',
               'r_summoner1_neturalMinionsKilled','r_summoner1_deaths','r_summoner1_tripleKills','r_summoner1_magicDamageDealtToChampions','r_summoner1_wardsKilled','r_summoner1_pentaKills','r_summoner1_damageSelfMitigated',
               'r_summoner1_largestCriticalStrike','r_summoner1_totalTimeCrowdControlDealt','r_summoner1_firstTowerKill','r_summoner1_magicDamageDealt','r_summoner1_totalScoreRank','r_summoner1_wardsPlaced','r_summoner1_totalDamageDealt',
               'r_summoner1_timeCCingOthers','r_summoner1_magicalDamageTaken','r_summoner1_largestKillingSpree','r_summoner1_totalDamageDealtToChampions','r_summoner1_physicalDamageDealtToChampions',
               'r_summoner1_neturalMinionsKilledTeamJungle','r_summoner1_totalMinionsKilled','r_summoner1_firstInhibitorAssist','r_summoner1_visionWardsBought','r_summoner1_objectivePlayerScore',
               'r_summoner1_kills','r_summoner1_firstTowerAssist','r_summoner1_combatPlayerScore','r_summoner1_inhibitorKills','r_summoner1_turretKills','r_summoner1_trueDamageTaken','r_summoner1_firstBloodAssist',
               'r_summoner1_assits','r_summoner1_goldSpent','r_summoner1_damageDealtToTurrets','r_summoner1_total_heal','r_summoner1_visionScore','r_summoner1_physicalDamageDealt','r_summoner1_firstBloodKill',
               'r_summoner1_longestTimeSpentLiving','r_summoner1_killingSprees','r_summoner1_trueDamageDealtToChampions','r_summoner1_doubleKills','r_summoner1_trueDamageDealth','r_summoner1_quadraKills',
               'r_summoner1_spell1','r_summoner1_spell2',
               
                #red team summoner 2 stats
               'r_summoner2_accountID','r_summoner2_position','r_summoner2_level','r_summoner2_champion','r_summoner2_champion_mastery','r_summoner2_champion_mastery','r_summoner2_champion_points_until_next_level',
               'r_summoner2_chest_granted','r_summoner2_champion_last_play_time','r_summoner2_champion_level','r_summoner2_champion_points_since_last_level','r_summoner2_tokens_earned','r_summoner2_total_mastery',
               'r_summoner2_item0','r_summoner2_item1','r_summoner2_item2','r_summoner2_item3','r_summoner2_item4','r_summoner2_item5','r_summoner2_item6','r_summoner2_totalUnitsHealed','r_summoner2_largestMultiKill',
               'r_summoner2_goldEarned','r_summoner2_firstInhibitorKill','r_summoner2_physicalDamageTaken','r_summoner2_totalPlayerScore','r_summoner2_championLevel','r_summoner2_damageDealtToObjectives','r_summoner2_totalDamageTaken',
               'r_summoner2_neturalMinionsKilled','r_summoner2_deaths','r_summoner2_tripleKills','r_summoner2_magicDamageDealtToChampions','r_summoner2_wardsKilled','r_summoner2_pentaKills','r_summoner2_damageSelfMitigated',
               'r_summoner2_largestCriticalStrike','r_summoner2_totalTimeCrowdControlDealt','r_summoner2_firstTowerKill','r_summoner2_magicDamageDealt','r_summoner2_totalScoreRank','r_summoner2_wardsPlaced','r_summoner2_totalDamageDealt',
               'r_summoner2_timeCCingOthers','r_summoner2_magicalDamageTaken','r_summoner2_largestKillingSpree','r_summoner2_totalDamageDealtToChampions','r_summoner2_physicalDamageDealtToChampions',
               'r_summoner2_neturalMinionsKilledTeamJungle','r_summoner2_totalMinionsKilled','r_summoner2_firstInhibitorAssist','r_summoner2_visionWardsBought','r_summoner2_objectivePlayerScore',
               'r_summoner2_kills','r_summoner2_firstTowerAssist','r_summoner2_combatPlayerScore','r_summoner2_inhibitorKills','r_summoner2_turretKills','r_summoner2_trueDamageTaken','r_summoner2_firstBloodAssist',
               'r_summoner2_assits','r_summoner2_goldSpent','r_summoner2_damageDealtToTurrets','r_summoner2_total_heal','r_summoner2_visionScore','r_summoner2_physicalDamageDealt','r_summoner2_firstBloodKill',
               'r_summoner2_longestTimeSpentLiving','r_summoner2_killingSprees','r_summoner2_trueDamageDealtToChampions','r_summoner2_doubleKills','r_summoner2_trueDamageDealth','r_summoner2_quadraKills',
               'r_summoner2_spell1','r_summoner2_spell2',

               #red team summoner 3 stats
               'r_summoner3_accountID','r_summoner3_position','r_summoner3_level','r_summoner3_champion','r_summoner3_champion_mastery','r_summoner3_champion_mastery','r_summoner3_champion_points_until_next_level',
               'r_summoner3_chest_granted','r_summoner3_champion_last_play_time','r_summoner3_champion_level','r_summoner3_champion_points_since_last_level','r_summoner3_tokens_earned','r_summoner3_total_mastery',
               'r_summoner3_item0','r_summoner3_item1','r_summoner3_item2','r_summoner3_item3','r_summoner3_item4','r_summoner3_item5','r_summoner3_item6','r_summoner3_totalUnitsHealed','r_summoner3_largestMultiKill',
               'r_summoner3_goldEarned','r_summoner3_firstInhibitorKill','r_summoner3_physicalDamageTaken','r_summoner3_totalPlayerScore','r_summoner3_championLevel','r_summoner3_damageDealtToObjectives','r_summoner3_totalDamageTaken',
               'r_summoner3_neturalMinionsKilled','r_summoner3_deaths','r_summoner3_tripleKills','r_summoner3_magicDamageDealtToChampions','r_summoner3_wardsKilled','r_summoner3_pentaKills','r_summoner3_damageSelfMitigated',
               'r_summoner3_largestCriticalStrike','r_summoner3_totalTimeCrowdControlDealt','r_summoner3_firstTowerKill','r_summoner3_magicDamageDealt','r_summoner3_totalScoreRank','r_summoner3_wardsPlaced','r_summoner3_totalDamageDealt',
               'r_summoner3_timeCCingOthers','r_summoner3_magicalDamageTaken','r_summoner3_largestKillingSpree','r_summoner3_totalDamageDealtToChampions','r_summoner3_physicalDamageDealtToChampions',
               'r_summoner3_neturalMinionsKilledTeamJungle','r_summoner3_totalMinionsKilled','r_summoner3_firstInhibitorAssist','r_summoner3_visionWardsBought','r_summoner3_objectivePlayerScore',
               'r_summoner3_kills','r_summoner3_firstTowerAssist','r_summoner3_combatPlayerScore','r_summoner3_inhibitorKills','r_summoner3_turretKills','r_summoner3_trueDamageTaken','r_summoner3_firstBloodAssist',
               'r_summoner3_assits','r_summoner3_goldSpent','r_summoner3_damageDealtToTurrets','r_summoner3_total_heal','r_summoner3_visionScore','r_summoner3_physicalDamageDealt','r_summoner3_firstBloodKill',
               'r_summoner3_longestTimeSpentLiving','r_summoner3_killingSprees','r_summoner3_trueDamageDealtToChampions','r_summoner3_doubleKills','r_summoner3_trueDamageDealth','r_summoner3_quadraKills',
               'r_summoner3_spell1','r_summoner3_spell2',

               #red team summoner 4 stats
               'r_summoner4_accountID','r_summoner4_position','r_summoner4_level','r_summoner4_champion','r_summoner4_champion_mastery','r_summoner4_champion_mastery','r_summoner4_champion_points_until_next_level',
               'r_summoner4_chest_granted','r_summoner4_champion_last_play_time','r_summoner4_champion_level','r_summoner4_champion_points_since_last_level','r_summoner4_tokens_earned','r_summoner4_total_mastery',
               'r_summoner4_item0','r_summoner4_item1','r_summoner4_item2','r_summoner4_item3','r_summoner4_item4','r_summoner4_item5','r_summoner4_item6','r_summoner4_totalUnitsHealed','r_summoner4_largestMultiKill',
               'r_summoner4_goldEarned','r_summoner4_firstInhibitorKill','r_summoner4_physicalDamageTaken','r_summoner4_totalPlayerScore','r_summoner4_championLevel','r_summoner4_damageDealtToObjectives','r_summoner4_totalDamageTaken',
               'r_summoner4_neturalMinionsKilled','r_summoner4_deaths','r_summoner4_tripleKills','r_summoner4_magicDamageDealtToChampions','r_summoner4_wardsKilled','r_summoner4_pentaKills','r_summoner4_damageSelfMitigated',
               'r_summoner4_largestCriticalStrike','r_summoner4_totalTimeCrowdControlDealt','r_summoner4_firstTowerKill','r_summoner4_magicDamageDealt','r_summoner4_totalScoreRank','r_summoner4_wardsPlaced','r_summoner4_totalDamageDealt',
               'r_summoner4_timeCCingOthers','r_summoner4_magicalDamageTaken','r_summoner4_largestKillingSpree','r_summoner4_totalDamageDealtToChampions','r_summoner4_physicalDamageDealtToChampions',
               'r_summoner4_neturalMinionsKilledTeamJungle','r_summoner4_totalMinionsKilled','r_summoner4_firstInhibitorAssist','r_summoner4_visionWardsBought','r_summoner4_objectivePlayerScore',
               'r_summoner4_kills','r_summoner4_firstTowerAssist','r_summoner4_combatPlayerScore','r_summoner4_inhibitorKills','r_summoner4_turretKills','r_summoner4_trueDamageTaken','r_summoner4_firstBloodAssist',
               'r_summoner4_assits','r_summoner4_goldSpent','r_summoner4_damageDealtToTurrets','r_summoner4_total_heal','r_summoner4_visionScore','r_summoner4_physicalDamageDealt','r_summoner4_firstBloodKill',
               'r_summoner4_longestTimeSpentLiving','r_summoner4_killingSprees','r_summoner4_trueDamageDealtToChampions','r_summoner4_doubleKills','r_summoner4_trueDamageDealth','r_summoner4_quadraKills',
               'r_summoner4_spell1','r_summoner4_spell2',

               #red team summoner 5 stats
               'r_summoner5_accountID','r_summoner5_position','r_summoner5_level','r_summoner5_champion','r_summoner5_champion_mastery','r_summoner5_champion_mastery','r_summoner5_champion_points_until_next_level',
               'r_summoner5_chest_granted','r_summoner5_champion_last_play_time','r_summoner5_champion_level','r_summoner5_champion_points_since_last_level','r_summoner5_tokens_earned','r_summoner5_total_mastery',
               'r_summoner5_item0','r_summoner5_item1','r_summoner5_item2','r_summoner5_item3','r_summoner5_item4','r_summoner5_item5','r_summoner5_item6','r_summoner5_totalUnitsHealed','r_summoner5_largestMultiKill',
               'r_summoner5_goldEarned','r_summoner5_firstInhibitorKill','r_summoner5_physicalDamageTaken','r_summoner5_totalPlayerScore','r_summoner5_championLevel','r_summoner5_damageDealtToObjectives','r_summoner5_totalDamageTaken',
               'r_summoner5_neturalMinionsKilled','r_summoner5_deaths','r_summoner5_tripleKills','r_summoner5_magicDamageDealtToChampions','r_summoner5_wardsKilled','r_summoner5_pentaKills','r_summoner5_damageSelfMitigated',
               'r_summoner5_largestCriticalStrike','r_summoner5_totalTimeCrowdControlDealt','r_summoner5_firstTowerKill','r_summoner5_magicDamageDealt','r_summoner5_totalScoreRank','r_summoner5_wardsPlaced','r_summoner5_totalDamageDealt',
               'r_summoner5_timeCCingOthers','r_summoner5_magicalDamageTaken','r_summoner5_largestKillingSpree','r_summoner5_totalDamageDealtToChampions','r_summoner5_physicalDamageDealtToChampions',
               'r_summoner5_neturalMinionsKilledTeamJungle','r_summoner5_totalMinionsKilled','r_summoner5_firstInhibitorAssist','r_summoner5_visionWardsBought','r_summoner5_objectivePlayerScore',
               'r_summoner5_kills','r_summoner5_firstTowerAssist','r_summoner5_combatPlayerScore','r_summoner5_inhibitorKills','r_summoner5_turretKills','r_summoner5_trueDamageTaken','r_summoner5_firstBloodAssist',
               'r_summoner5_assits','r_summoner5_goldSpent','r_summoner5_damageDealtToTurrets','r_summoner5_total_heal','r_summoner5_visionScore','r_summoner5_physicalDamageDealt','r_summoner5_firstBloodKill',
               'r_summoner5_longestTimeSpentLiving','r_summoner5_killingSprees','r_summoner5_trueDamageDealtToChampions','r_summoner5_doubleKills','r_summoner5_trueDamageDealth','r_summoner5_quadraKills',
               'r_summoner5_spell1','r_summoner5_spell2',

               #results of the match (one hot vector that will be what we are trying to predict)
               'b_win','r_win']
   
    def __init__(self,api_key_location,region,training_data_location):
        self.api_key_location = api_key_location
        f = open(self.api_key_location)
        self.api_key = f.readline()
        f.close()
        self.region = 'na1'
        self.training_data_location = training_data_location
    
    @staticmethod
    def make_training_data():
        player_puller = PlayerDataPuller(DataSetMaker.api_key,DataSetMaker.region)
        match_puller = MatchDataPuller(DataSetMaker.api_key,DataSetMaker.region)
        champion_puller = ChampionMasteryDataPuller(DataSetMaker.api_key,DataSetMaker.region)
        f = open(training_data_location)
        
        for i in range(1,10001):
            pass

        f.close()
def main():
    test = ['b_tower_kills','b_rift_herald_kills','b_first_blood','b_inhibitor_kills','b_first_baron','b_first_dragon','b_dragon_kills','b_baron_kills','b_first_inhibitor','b_first_tower','b_first_rift_herald']
    print(len(test))    
    print(DataSetMaker.columns[96])
    print(DataSetMaker.columns[97])
main()