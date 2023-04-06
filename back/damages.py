import cassiopeia as cass
from collections import Counter
import csv
import matplotlib.pyplot as plt
import numpy as np

def test():
    cass.set_riot_api_key('RGAPI-8e88a106-c955-4d6c-99d6-688f4d09c0ae')
    pseudo = "Seieki No Jutsu"
    me = cass.get_summoner(name = pseudo, region="EUW")
    """
    print(me.match_history.search("Sightstone").sizeof)

    for game in me.match_history:
        print(game. )
    """
    print(me.level)

    matches = me.match_history[50:350]
    list_champs = []
    damage = 0
    mat = 0
    list_dmg_d = []
    list_dmg_t = []
    list_dmg_m = []
    list_ccs = []
    list_tcc = []
    list_time = []

    

    for match in matches:
        #print(match.participants[me].stats.__dir__())
        if (str(match.mode) == "GameMode.aram" and match.participants[me].stats.time_played > 400):
        
            champion = match.participants[me].champion.name
            list_champs.append(champion)
            list_dmg_d.append(match.participants[me].stats.total_damage_dealt_to_champions)
            list_dmg_t.append(match.participants[me].stats.total_damage_taken)
            list_dmg_m.append(match.participants[me].stats.damage_self_mitigated)
            list_ccs.append(match.participants[me].stats.total_time_cc_dealt)
            list_tcc.append(match.participants[me].stats.time_CCing_others)
            list_time.append(match.participants[me].stats.time_played)


    


    #print(Counter(list_champs))
    #print(len(set(list_champs)))
    """
    print(list_champs)
    print(list_dmg_d)
    print(list_dmg_t)
    print(list_dmg_m)
    print(list_ccs)
    print(list_tcc)
    """

    list_set_champs = []
    list_tot = []

    for i in range(len(list_champs)):
        index_champ = 0
        if list_champs[i] in list_set_champs:
            index_champ = list_set_champs.index(list_champs[i])
            list_temp = [list_dmg_d[i], list_dmg_t[i], list_dmg_m[i], list_ccs[i], list_tcc[i], list_time[i], 1]
            list_tot[index_champ] = [list_tot[index_champ][j] + list_temp[j] for j in range(len(list_temp))]
        
        else:
            list_set_champs.append(list_champs[i])
            list_tot.append([list_dmg_d[i], list_dmg_t[i], list_dmg_m[i], list_ccs[i], list_tcc[i], list_time[i], 1])

    print(list_set_champs)
    print(list_tot)

    
    plt.figure(1)
    plt.title("Dégâts selon temps")
    plt.xlabel("Temps")
    plt.ylabel("Dégâts")
    plt.scatter(list_time, list_dmg_d, s=10)
    c1, b1, a1 = np.polyfit(list_time, list_dmg_d, deg=2)
    xseq = np.linspace(0, max(list_time), num=100)
    plt.plot(xseq, a1 + b1*xseq + c1*xseq*xseq)

    plt.figure(2)
    plt.title("Dégâts subis selon temps")
    plt.xlabel("Temps")
    plt.ylabel("Dégâts subis")
    plt.scatter(list_time, list_dmg_t, s=10)
    c2, b2, a2 = np.polyfit(list_time, list_dmg_t, deg=2)
    plt.plot(xseq, a2 + b2*xseq + c2*xseq*xseq)

    plt.figure(3)
    plt.title("Dégâts mitigés selon temps")
    plt.xlabel("Temps")
    plt.ylabel("Dégâts mitigés")
    plt.scatter(list_time, list_dmg_m, s=10)
    c3, b3, a3 = np.polyfit(list_time, list_dmg_m, deg=2)
    plt.plot(xseq, a3 + b3*xseq + c3*xseq*xseq)
    
    plt.show()



    """
    with open(pseudo + '.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for i in range(len(list_set_champs)):
            spamwriter.writerow([list_set_champs[i]] + list_tot[i])                                 
    """
        

"""
['_data', '_ParticipantStats__match', '_ParticipantStats__participant', '__module__', '_data_types', 'from_data', 'kda', 'deaths', 'assists', 'kills', 'baron_kills', 'bounty_level', 'champion_experience', 'level', 
'champion_transform', 'consumables_purchased', 
'damage_dealt_to_buildings', 'damage_dealt_to_objectives', 'damage_dealt_to_turrets', 'damage_self_mitigated', 'vision_wards_bought', 'vision_wards_placed', 'double_kills', 'dragon_kills', 'first_blood_assist', 
'first_blood_kill', 'first_tower_assist', 'first_tower_kill', 'gold_earned', 'gold_spent', 'inhibitor_kills', 'inhibitor_takedowns', 'inhibitors_lost', 'items', 'items_purchased', 'killing_sprees', 
'largest_critical_strike', 'largest_killing_spree', 'largest_multi_kill', 'longest_time_spent_living', 'magic_damage_dealt', 'magic_damage_dealt_to_champions', 'magic_damage_taken', 'neutral_minions_killed', 
'nexus_kills', 'nexus_lost', 'nexus_takedowns', 'objectives_stolen', 'objectives_stolen_assists', 'penta_kills', 'physical_damage_dealt', 'physical_damage_dealt_to_champions', 'physical_damage_taken', 'quadra_kills',
 'sight_wards_bought', 'spell_1_casts', 'spell_2_casts', 'spell_3_casts', 'spell_4_casts', 'summoner_spell_1_casts', 'summoner_spell_2_casts', 'time_CCing_others', 'time_played', 'total_damage_dealt', 
 'total_damage_dealt_to_champions', 'total_damage_shielded_on_teammates', 'total_damage_taken', 'total_heal', 'total_heals_on_teammates', 'total_minions_killed', 'total_time_cc_dealt', 'total_time_spent_dead', 
 'total_units_healed', 'triple_kills', 'true_damage_dealt', 'true_damage_dealt_to_champions', 'true_damage_taken', 'turret_kills', 'turret_takedowns', 'turrets_lost', 'unreal_kills', 'vision_score', 'wards_killed', 
 'wards_placed', 'win', '__doc__', '__contains__', '_renamed', '__init__', '__str__', '__call__', 'to_dict', 'to_json', '__json__', '__dict__', '__weakref__', '__repr__', '__hash__', '__getattribute__', 
 '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', 
 '__dir__', '__class__']

"""

def test2():

    cass.set_riot_api_key('RGAPI-83fc614a-c91b-4ed6-92d8-0f6b61a02ac5')
    me = cass.get_summoner(name = "Seieki No Jutsu", region="EUW")

    matches = me.match_history[10:11]

    for match in matches:
        print(match.participants[me].stats.kills)
        print(match.participants[me].stats.deaths) 
        print(match.participants[me].stats.assists)
        print(match.participants[me].stats.win)


def main():
    print("hello")
    test()

main()