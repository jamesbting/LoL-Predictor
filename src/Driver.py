from DataPuller import PlayerDataPuller
#file to test other piles
if __name__ == "__main__":
    api_key = 'RGAPI-3117808d-74db-4bbc-959b-c966789344a6'
    region = 'na1'
    puller = PlayerDataPuller(api_key,region)
    player_data = puller.getPlayerInfoByName("TheRipsticker")
    print(player_data)
    puller.set_region("EUW")