from selenium import webdriver
from pandas import *
import pandas
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import *
import pickle
import numpy as np


big_dict = pickle.load(open("plus10_included.p", "rb"))

total_shots = 0

league_averages = {'0-2 Feet (Very Tight)': {'Layups': {'made': 0, 'att': 0}, "Mid-Range": {'made': 0, 'att': 0}, '3pt Range': {'made': 0, 'att': 0}},
                    '2-4 Feet (Tight)': {'Layups': {'made': 0, 'att': 0}, "Mid-Range": {'made': 0, 'att': 0}, '3pt Range': {'made': 0, 'att': 0}},
                    '4-6 Feet (Open)': {'Layups': {'made': 0, 'att': 0}, "Mid-Range": {'made': 0, 'att': 0}, '3pt Range': {'made': 0, 'att': 0}},
                    '6+ Feet (Wide Open)': {'Layups': {'made': 0, 'att': 0}, "Mid-Range": {'made': 0, 'att': 0}, '3pt Range': {'made': 0, 'att': 0}}}

print(big_dict['Devin Booker'])

for player in big_dict:
    for range in big_dict[player]:
        for type in big_dict[player][range]:
            if type in ['Layups', 'Mid-Range'] and len(big_dict[player][range][type].keys()) > 1:
                league_averages[range][type]['made'] += int(big_dict[player][range][type]['2FGM'])
                league_averages[range][type]['att'] += int(big_dict[player][range][type]['2FGA'])
            elif type in ['3pt Range'] and len(big_dict[player][range][type].keys()) > 1:
                league_averages[range][type]['made'] += int(big_dict[player][range][type]['3PM'])
                league_averages[range][type]['att'] += int(big_dict[player][range][type]['3PA'])

print(league_averages)
averages = []
for range in league_averages:
    for type in league_averages[range]:
        if league_averages[range][type]['att'] !=0:
            perc = league_averages[range][type]['made']/league_averages[range][type]['att']
            averages.append(perc)
        else:
            averages.append(0)

types = ['Very Tight Layups', 'Very Tight Mid-Range', 'Very Tight 3pt Range',
         'Tight Layups', 'Tight Mid-Range', 'Tight 3pt Range',
         'Open Layups', 'Open Mid-Range', 'Open 3pt Range',
         'Wide Open Layups', 'Wide Open Mid-Range', 'Wide Open 3pt Range']


book_averages = {'0-2 Feet (Very Tight)': {'Layups': {'made': 0, 'att': 0}, "Mid-Range": {'made': 0, 'att': 0}, '3pt Range': {'made': 0, 'att': 0}},
                    '2-4 Feet (Tight)': {'Layups': {'made': 0, 'att': 0}, "Mid-Range": {'made': 0, 'att': 0}, '3pt Range': {'made': 0, 'att': 0}},
                    '4-6 Feet (Open)': {'Layups': {'made': 0, 'att': 0}, "Mid-Range": {'made': 0, 'att': 0}, '3pt Range': {'made': 0, 'att': 0}},
                    '6+ Feet (Wide Open)': {'Layups': {'made': 0, 'att': 0}, "Mid-Range": {'made': 0, 'att': 0}, '3pt Range': {'made': 0, 'att': 0}}}

for player in big_dict:
    if player == 'Devin Booker':
        for range in big_dict[player]:
            for type in big_dict[player][range]:
                if type in ['Layups', 'Mid-Range'] and len(big_dict[player][range][type].keys()) > 1:
                    book_averages[range][type]['made'] += int(big_dict[player][range][type]['2FGM'])
                    book_averages[range][type]['att'] += int(big_dict[player][range][type]['2FGA'])
                elif type in ['3pt Range'] and len(big_dict[player][range][type].keys()) > 1:
                    book_averages[range][type]['made'] += int(big_dict[player][range][type]['3PM'])
                    book_averages[range][type]['att'] += int(big_dict[player][range][type]['3PA'])

bookavg = []

for range in book_averages:
    for type in book_averages[range]:
        if league_averages[range][type]['att'] !=0:
            perc = book_averages[range][type]['made']/book_averages[range][type]['att']
            bookavg.append(perc)
        else:
            bookavg.append(0)



fig = plt.figure()
axs = fig.add_subplot(111)
axs.scatter(types, bookavg, label= 'Devin Booker', color='purple')
axs.scatter(types, averages, label = 'league_averages')

plt.xticks(rotation = -30)


plt.legend(loc='upper left');
plt.style.use('fivethirtyeight')

plt.show()

"""
for range in big_dict['Devin Booker']:
    for type in big_dict['Devin Booker'][range]:
        if type in ['Layups', 'Mid-Range'] and len(big_dict[player][range][type].keys()) > 1:
            print(range, type)
            made = float(big_dict['Devin Booker'][range][type]['2FGM'])
            att = float(big_dict['Devin Booker'][range][type]['2FGA'])
            bookavg.append(made/att)
            continue
        elif type in ['3pt Range'] and len(big_dict[player][range][type].keys()) > 1:
            print(range, type)
            made = float(big_dict['Devin Booker'][range][type]['3PM'])
            att = float(big_dict['Devin Booker'][range][type]['3PA'])
            bookavg.append(made/att)
"""
