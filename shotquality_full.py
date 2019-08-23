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
    score = 0
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
                temp = (player_perc - league_perc)*(att/int(games_played[player]))*q_mult
                score += temp
            elif type in ['3pt Range'] and len(main[player][shotrange][type].keys()) > 1:
                att = int(main[player][shotrange][type]['3PA'])
                makes = int(main[player][shotrange][type]['3PM'])
                if att > 0:
                    player_perc = makes/att
                else:
                    player_perc = 0
                league_perc = league_averages[shotrange][type]
                q_mult = quality_multiplers[shotrange][type]
                temp = (player_perc - league_perc)*(att/int(games_played[player]))*1.5*q_mult
                score += temp
    player_quality[player] = score

sorted_pq = sorted(player_quality.items(), key=operator.itemgetter(1))
values = list(player_quality.values())
values.sort()
names = []
for tup in sorted_pq:
    names.append(tup[0])



fig, axs = plt.subplots(figsize=(20,5))
axs.scatter(names, values)

plt.xticks(rotation = -90)

#plt.style.use('fivethirtyeight')


plt.show()
