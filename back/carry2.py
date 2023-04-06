import cassiopeia as cass
from collections import Counter
import csv
import matplotlib.pyplot as plt
import numpy as np

def test():
    cass.set_riot_api_key('RGAPI-d048c676-d752-4533-872c-247933f6727d')
    pseudo = "Reine Shérazade"
    me = cass.get_summoner(name = pseudo, region="EUW")
    """
    print(me.match_history.search("Sightstone").sizeof)

    for game in me.match_history:
        print(game. )
    """
    print(me.level)

    matches = me.match_history[0:50]
    list_champs = []
    list_dmg_d = []
    list_dmg_t = []
    list_dmg_m = []
    list_ccs = []
    list_tcc = []
    list_deaths = []
    list_shield = []
    list_heal = []

    list_index_player = []
    

    for match in matches:
        #print(match.participants[me].stats.__dir__())
        if (str(match.mode) == "GameMode.aram" and match.participants[me].stats.time_played > 400):
            
            for index_player in range(10):
                if match.participants[me].champion.name == match.participants[index_player].champion.name:
                    break
            
            team = 0
            if index_player > 4:
                team = 5

            list_index_player.append(index_player - team)


            list_temp_champs = []
            list_temp_dmg_d = []
            list_temp_dmg_t = []
            list_temp_dmg_m = []
            list_temp_ccs = []
            list_temp_tcc = []
            list_temp_deaths = []
            list_temp_shield = []
            list_temp_heal = []

            for j in range(team, team+5):
                        
                list_temp_champs.append(match.participants[j].champion.name)
                list_temp_dmg_d.append(match.participants[j].stats.total_damage_dealt_to_champions)
                list_temp_dmg_t.append(match.participants[j].stats.total_damage_taken)
                list_temp_dmg_m.append(match.participants[j].stats.damage_self_mitigated)
                list_temp_ccs.append(match.participants[j].stats.time_CCing_others)
                list_temp_tcc.append(match.participants[j].stats.total_time_cc_dealt)
                list_temp_deaths.append(match.participants[j].stats.deaths) 
                list_temp_shield.append(match.participants[j].stats.total_damage_shielded_on_teammates)
                list_temp_heal.append(match.participants[j].stats.total_heals_on_teammates)

            list_champs.append(list_temp_champs)
            list_dmg_d.append(list_temp_dmg_d)
            list_dmg_t.append(list_temp_dmg_t)
            list_dmg_m.append(list_temp_dmg_m)
            list_ccs.append(list_temp_ccs)
            list_tcc.append(list_temp_tcc)
            list_deaths.append(list_temp_deaths)
            list_shield.append(list_temp_shield)
            list_heal.append(list_temp_heal)
    

    list_carry = []
    
    dd = 2.55
    dt = 1.85
    ccs = 0.40
    tcc = 0.20

    """
    for i in range(len(list_champs)):
        
        j = list_index_player[i]

        carry = dd * ((list_dmg_d[i][j] + 1.2 * list_heal[i][j]) / (sum(list_dmg_d[i]) + 1.2 * sum(list_heal[i]))) + \
                dt * ((list_dmg_t[i][j] + 1.4 * list_shield[i][j] + list_dmg_m[i][j]) / 
                      (sum(list_dmg_t[i]) + 1.4 * sum(list_shield[i]) + sum(list_dmg_m[i]))) + \
                ccs * (list_ccs[i][j] / sum(list_ccs[i])) + \
                tcc * (list_tcc[i][j] / sum(list_tcc[i]))
            
        list_carry.append(carry)


    list_set_champs = []
    list_set_carry = []


    for i in range(len(list_champs)):
        index_champ = 0
        j = list_index_player[i]

        if list_champs[i][j] in list_set_champs:
            index_champ = list_set_champs.index(list_champs[i][j])

            list_set_carry[index_champ] = [list_set_carry[index_champ][0] + list_carry[i], list_set_carry[index_champ][1] + 1]
        
        else:
            list_set_champs.append(list_champs[i][j])

            list_set_carry.append([list_carry[i], 1])

    for i in range(len(list_set_carry)):

        print(list_set_champs[i], ' : ', round(list_set_carry[i][0] / list_set_carry[i][1], 2), " | ", list_set_carry[i][1])


    """
    for i in range(len(list_champs)):
        
        for j in range(5):

            carry = dd * ((list_dmg_d[i][j] + 1.2 * list_heal[i][j]) / (sum(list_dmg_d[i]) + 1.2 * sum(list_heal[i]))) + \
                dt * ((list_dmg_t[i][j] + 1.4 * list_shield[i][j] + list_dmg_m[i][j]) / 
                      (sum(list_dmg_t[i]) + 1.4 * sum(list_shield[i]) + sum(list_dmg_m[i]))) + \
                ccs * (list_ccs[i][j] / sum(list_ccs[i])) + \
                tcc * (list_tcc[i][j] / sum(list_tcc[i]))
            
            print(list_champs[i][j], " : ", round(carry, 2), list_ccs[i][j], list_tcc[i][j], list_shield[i][j], list_heal[i][j])

        print()

    

        

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




def main():
    print("hello")
    test()

main()