from selenium import webdriver
from pandas import *
import pandas
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import *
import pickle
import numpy as np
import collections
import operator




main = pickle.load(open("plus10_included.p", "rb"))
games_played = pickle.load(open("games_played.p", "rb"))
efg_perc = pickle.load(open("efg_perc.p", "rb"))


league_averages_totals = {'0-2 Feet (Very Tight)': {'Layups': {'made': 10652, 'att': 23109}, 'Mid-Range': {'made': 619, 'att': 1819}, '3pt Range': {'made': 177, 'att': 696}},
                          '2-4 Feet (Tight)': {'Layups': {'made': 0, 'att': 0}, 'Mid-Range': {'made': 5611, 'att': 14669}, '3pt Range': {'made': 2369, 'att': 8130}},
                          '4-6 Feet (Open)': {'Layups': {'made': 0, 'att': 0}, 'Mid-Range': {'made': 8028, 'att': 19312}, '3pt Range': {'made': 9590, 'att': 28323}},
                          '6+ Feet (Wide Open)': {'Layups': {'made': 0, 'att': 0}, 'Mid-Range': {'made': 3364, 'att': 7494}, '3pt Range': {'made': 15691, 'att': 41276}}}

hm = {'Layups': 0.4609459517936735, 'Mid-Range': 0.407030997367, '3pt Range': 0.354823079375}


league_averages = {'0-2 Feet (Very Tight)': {'Layups': 0.4609459517936735, "Mid-Range": 0.3402968664101155, '3pt Range': 0.2543103448275862},
                    '2-4 Feet (Tight)': {'Layups': 0, "Mid-Range": 0.38250732837957596, '3pt Range': 0.291389913899139},
                    '4-6 Feet (Open)': {'Layups': 0, "Mid-Range": 0.41570008285004145, '3pt Range': 0.33859407548635384},
                    '6+ Feet (Wide Open)': {'Layups': 0, "Mid-Range": 0.4488924472911663, '3pt Range': 0.3801482701812191}}

quality_multiplers = {'0-2 Feet (Very Tight)': {'Layups': 1, "Mid-Range": 0.407030997367/0.3402968664101155, '3pt Range': 0.354823079375/0.2543103448275862},
                        '2-4 Feet (Tight)': {'Layups': 1, "Mid-Range": 0.407030997367/0.38250732837957596, '3pt Range': 0.354823079375/0.291389913899139},
                        '4-6 Feet (Open)': {'Layups': 1, "Mid-Range": 0.407030997367/0.41570008285004145, '3pt Range': 0.354823079375/0.33859407548635384},
                        '6+ Feet (Wide Open)': {'Layups': 1, "Mid-Range": 0.407030997367/0.4488924472911663, '3pt Range': 0.354823079375/0.3801482701812191}}


player_quality = {}
for player in main:
    make_score = 0
    att_score = 0
    for shotrange in main[player]:
        for type in main[player][shotrange]:
            if type in ['Layups', 'Mid-Range'] and len(main[player][shotrange][type].keys()) > 1:

                att = int(main[player][shotrange][type]['2FGA'])
                makes = int(main[player][shotrange][type]['2FGM'])
                if att > 0:
                    player_perc = makes/att
                else:
                    player_perc = 0

                league_perc = league_averages[shotrange][type]
                q_mult = quality_multiplers[shotrange][type]
                temp = makes*q_mult
                make_score += temp
                att_score += att
            elif type in ['3pt Range'] and len(main[player][shotrange][type].keys()) > 1:
                att = int(main[player][shotrange][type]['3PA'])
                makes = int(main[player][shotrange][type]['3PM'])
                if att > 0:
                    player_perc = makes/att
                else:
                    player_perc = 0
                league_perc = league_averages[shotrange][type]
                q_mult = quality_multiplers[shotrange][type]
                temp = makes*q_mult*1.5
                make_score += temp
                att_score += att
    score = make_score/att_score
    player_quality[player] = score

sorted_pq = sorted(player_quality.items(), key=operator.itemgetter(1))
values = list(player_quality.values())
values.sort()
names = []
for tup in sorted_pq:
    names.append(tup[0])

#print(sorted_pq)



player_quality_bum = player_quality.copy()
player_quality_qualified = player_quality_bum.copy()

for player in player_quality_bum:

    att = 0

    for defense in main[player]:
        for type in main[player][defense]:
            if type in ['Layups', 'Mid-Range'] and len(main[player][defense][type].keys()) > 1:
                att += int(main[player][defense][type]['2FGA'])
            elif type in ['3pt Range'] and len(main[player][defense][type].keys()) > 1:
                att += int(main[player][defense][type]['3PA'])


sorted_pqq = list(sorted(list(player_quality_qualified.items()), key=operator.itemgetter(1), reverse=True))

filtered_shotqual = {}
for tup in range(len(sorted_pqq)):
    if sorted_pqq[tup][0] in efg_perc:
        filtered_shotqual[sorted_pqq[tup][0]] = sorted_pqq[tup][1]



change_in_ranking = {}
for i in range(len(list(filtered_shotqual.keys()))):
    new_rank = i
    old_rank = list(efg_perc.keys()).index(list(filtered_shotqual.keys())[i])
    change = old_rank - new_rank

    change_in_ranking[list(filtered_shotqual.keys())[i]] = change

for key in filtered_shotqual:
    old_perc = float(efg_perc[key])
    new_perc = round(filtered_shotqual[key]*100,1)

    print('|  ' + key + '  |  ' + str(new_perc) + "  |  " + str(old_perc) + "  |  ")


sorted_ranking = list(sorted(list(change_in_ranking.items()), key=operator.itemgetter(1), reverse=True))

fig = plt.figure()
axs = fig.add_subplot(111)

efgkeys = list(efg_perc.keys())
efgkeys.reverse()

temp = list(efg_perc.values())
efgvals = []
for i in range(len(temp)):
    efgvals.append(float(temp[i]))
efgvals.reverse()

axs.scatter(efgkeys, efgvals, label = 'league_averages')

plt.xticks(rotation = -30)

plt.legend(loc='upper left');
plt.style.use('fivethirtyeight')


#plt.show()


"""
values = list(player_quality_qualified.values())
values.sort()
names = []
for tup in sorted_pqq:
    names.append(tup[0])


change_in_perc = {}

for player in player_quality_qualified:
    change = player_quality_qualified[player]*100 - float(efg_perc[player])
    change_in_perc[player] = change


sorted_change = sorted(change_in_perc.items(), key=operator.itemgetter(1))

change_in_ranking = {}

for tuppy in range(len(sorted_pqq)):
    change_in_ranking[sorted_pqq[tuppy][0]] = sorted_pqq[tuppy][1]

efg = []
for key in efg_perc:
    if key in change_in_ranking:
        efg.append(key)




print(efg)
print(list(change_in_ranking.keys()))
"""
