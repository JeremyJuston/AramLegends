import cassiopeia as cass
from collections import Counter
import csv


def get_champions_list2(username):

    return ["1", "2", username]



def get_champions_list(username):

    cass.set_riot_api_key('RGAPI-83fc614a-c91b-4ed6-92d8-0f6b61a02ac5')
    me = cass.get_summoner(name = username, region="EUW")

    matches = me.match_history[10:50]
    
    list_set_champs, list_tot = create_lists_from_matches(me, matches)

    
    return list_to_return(list_set_champs, list_tot)



def create_lists_from_matches(me, matches):
    
    list_champs, list_tot = create_list_tot(me, matches)
    
    return create_lists_from_list_tot(list_champs, list_tot)



def create_list_tot(me, matches):

    list_champs = []
    list_dmg_d = []
    list_dmg_t = []
    list_dmg_m = []
    list_ccs = []
    list_tcc = []
    list_kills = []
    list_deaths = []
    list_assists = []
    list_win = []
    list_time = []
    

    for match in matches:
        #print(match.participants[me].stats.__dir__())
        if (str(match.mode) == "GameMode.aram"):
        
            champion = match.participants[me].champion.name
            list_champs.append(champion)
            
            list_dmg_d.append(match.participants[me].stats.total_damage_dealt_to_champions)
            list_dmg_t.append(match.participants[me].stats.total_damage_taken)
            list_dmg_m.append(match.participants[me].stats.damage_self_mitigated)
            list_ccs.append(match.participants[me].stats.time_CCing_others)
            list_tcc.append(match.participants[me].stats.total_time_cc_dealt)
            list_kills.append(match.participants[me].stats.kills)
            list_deaths.append(match.participants[me].stats.deaths) 
            list_assists.append(match.participants[me].stats.assists)
            list_win.append(int(match.participants[me].stats.win))
            list_time.append(match.participants[me].stats.time_played)

    list_tot = [list_dmg_d, list_dmg_t, list_dmg_m, list_ccs, list_tcc, list_kills, list_deaths, list_assists, list_time, list_win]


    return list_champs, list_tot



def create_lists_from_list_tot(list_champs, list_tot):
    list_set_champs = []
    list_stats = []

    for i in range(len(list_champs)):
        index_champ = 0
        list_temp = []

        if list_champs[i] in list_set_champs:
            index_champ = list_set_champs.index(list_champs[i])

            for j in range(len(list_tot)):
                list_temp.append(list_tot[j][i])
            list_temp.append(1)

            list_stats[index_champ] = [list_stats[index_champ][j] + list_temp[j] for j in range(len(list_temp))]
        
        else:
            list_set_champs.append(list_champs[i])

            for j in range(len(list_tot)):
                list_temp.append(list_tot[j][i])

            list_temp.append(1)

            list_stats.append(list_temp)


    return list_set_champs, list_stats
    


def list_to_return(list_set_champs, list_tot):
    
    list_to_return = []

    for i in range(len(list_set_champs)):
        list_to_return.append([list_set_champs[i]])

        for j in range(len(list_tot[i]) - 2):
            decimales = 0
            if j > 5 and j < 9:
                decimales = 1
            list_to_return[i].append(round(list_tot[i][j] / list_tot[i][-1], decimales))
        
        list_to_return[i].append(round(list_tot[i][-2] / list_tot[i][-1] * 100))
        list_to_return[i].append(list_tot[i][-1])

    return list_to_return


def main():
    return 0