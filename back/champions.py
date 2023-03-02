import cassiopeia as cass
from collections import Counter
import csv


def get_champions_list(username):
    return ["1", "2", username]



def get_champions_list2(username):
    cass.set_riot_api_key('RGAPI-9eb9bec8-7d12-4cfa-839b-cca22d53df20')
    me = cass.get_summoner(name = username, region="EUW")

    matches = me.match_history[0:400]
    list_champs = []
    damage = 0
    mat = 0
    list_dmg_d = []
    list_dmg_t = []
    list_dmg_m = []
    list_ccs = []
    list_tcc = []

    

    for match in matches:
        #print(match.participants[me].stats.__dir__())
        if (str(match.mode) == "GameMode.aram"):
        
            champion = match.participants[me].champion.name
            list_champs.append(champion)
            list_dmg_d.append(match.participants[me].stats.total_damage_dealt_to_champions)
            list_dmg_t.append(match.participants[me].stats.total_damage_taken)
            list_dmg_m.append(match.participants[me].stats.damage_self_mitigated)
            list_ccs.append(match.participants[me].stats.total_time_cc_dealt)
            list_tcc.append(match.participants[me].stats.time_CCing_others)


    list_set_champs = []
    list_tot = []

    for i in range(len(list_champs)):
        index_champ = 0
        if list_champs[i] in list_set_champs:
            index_champ = list_set_champs.index(list_champs[i])
            list_temp = [list_dmg_d[i], list_dmg_t[i], list_dmg_m[i], list_ccs[i], list_tcc[i], 1]
            list_tot[index_champ] = [list_tot[index_champ][j] + list_temp[j] for j in range(len(list_temp))]
        
        else:
            list_set_champs.append(list_champs[i])
            list_tot.append([list_dmg_d[i], list_dmg_t[i], list_dmg_m[i], list_ccs[i], list_tcc[i], 1])

    list_to_return = []

    for i in range(len(list_set_champs)):
        list_to_return.append([list_set_champs[i]])
        for j in range(len(list_tot[i])-1):
            list_to_return[i].append(round(list_tot[i][j]/list_tot[i][-1]))
        list_to_return[i].append(list_tot[i][-1])



    return list_to_return


def main():
    return 0