import wargaming



def get_ship_information(api, ship_ids):
    index = 0
    data = {}
    while (index < len(ship_ids)):
        ids = ",".join(ship_ids[index:index+100])
        data.update(dict(api.encyclopedia.ships(ship_id=ids, fields="images.small,name,type")))
        index += 100
    return data

def get_relevant_stats(api, playerid):

    stats = dict(api.ships.stats(account_id=playerid, extra="pvp_solo,rank_solo"))[playerid]
    revisedStats = []
    ship_ids = []

    for ship in stats:
        if(ship["battles"]<10):
            continue

        if(ship["pvp_solo"]["battles"]<10):
            del ship["pvp_solo"]
        if(ship["rank_solo"]["battles"]<10):
            del ship["rank_solo"]
        ship_ids.append(str(ship["ship_id"]))
        revisedStats.append(ship)

    stats = []
    for ship_id, shipdata in get_ship_information(api, ship_ids).iteritems():
        new_id = str(ship_id)
        for i in range(len(revisedStats)):
            if(str(revisedStats[i]["ship_id"]) == new_id):
                if shipdata:
                    revisedStats[i].update(shipdata)
                    stats.append(revisedStats[i])
                #revisedStats[i].update(shipdata)

    print stats

if __name__ == "__main__":
    wows = wargaming.WoWS('demo', region='na', language='en')
    get_relevant_stats(wows,"1003490729")
    #createSignatureGif("input.gif", "output2.gif", False)
