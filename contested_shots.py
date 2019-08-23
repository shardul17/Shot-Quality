from selenium import webdriver
from pandas import *
import pandas
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import *
import pickle


path_to_chromedriver = 'chromedriver.exe' # Path to access a chrome driver
browser = webdriver.Chrome(executable_path=path_to_chromedriver)

url = 'https://stats.nba.com/players/advanced/?sort=EFG_PCT&dir=-1&CF=FGA*G*300:GP*G*50'
#url = 'https://stats.nba.com/leaders/'

browser.get(url)



browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select/option[1]').click()
#
# browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[3]/div/div/select/option[1]').click()

table = browser.find_element_by_class_name('nba-stat-table__overflow')


player_ids = []
player_names = []
player_stats = []

count = 1
for line_id, lines in enumerate(table.text.split('\n')):
    #print(lines)
    if line_id == 0:
        pass
        #column_names = lines.split(' ')[1:]

    elif line_id > 0:
        if count == 1:
            player_ids.append(lines)
            count += 1
        # if line_id % 3 == 2:
        #     player_names.append(lines)
        elif count == 2:
            player_names.append(lines)

            count += 1
        elif count == 3:
            player_stats.append( [i for i in lines.split(' ')] )
            count = 1


master_dict = pickle.load(open("plus10_included.p", "rb"))



column_names = ['TEAM', 'AGE', 'GP', 'G', 'FREQ', 'FGM', 'FGA', 'FG%', 'EFG%',
            '2FG FREQ', '2FGM', '2FGA', '2FG%', '3FG FREQ', '3PM', '3PA', '3P%']

efg_perc = {}

for i in range(len(player_names)):
     efg_perc[player_names[i]] = player_stats[i][15]
    #efg_perc[player_names[i]] = player_stats[i][16]


"""
for i in range(len(player_names)):
    if player_names[i] not in master_dict:
        master_dict[player_names[i]] = {'0-2 Feet (Very Tight)': {'Layups': {}, 'Mid-Range': {}, '3pt Range': {}},
                                        '2-4 Feet (Tight)': {'Layups': {}, 'Mid-Range': {}, '3pt Range': {}},
                                        '4-6 Feet (Open)': {'Layups': {}, 'Mid-Range': {}, '3pt Range': {}},
                                        '6+ Feet (Wide Open)': {'Layups': {}, 'Mid-Range': {}, '3pt Range': {}}
                                        }

    # if player_names[i] not in master_dict:
    #     master_dict[player_names[i]] = {'6+ Feet (Wide Open)': {}}
    # else:
    #     master_dict[player_names[i]]['6+ Feet (Wide Open)'] = {}


    for j in range(len(column_names)):
        curr_range = '0-2 Feet (Very Tight)'
        if column_names[j] in ['2FG FREQ', '2FGM', '2FGA', '2FG%']:
            if column_names[j] == '2FG FREQ':
                if '2FG FREQ' in master_dict[player_names[i]][curr_range]['Mid-Range']:
                    freq = str(float(player_stats[i][j][:-1]) - float(master_dict[player_names[i]][curr_range]['Mid-Range']['2FG FREQ'][:-1])) + '%'
                    master_dict[player_names[i]][curr_range]['Layups'][column_names[j]] = freq
                else:
                    freq = str(float(player_stats[i][j][:-1]))
                    master_dict[player_names[i]][curr_range]['Layups'][column_names[j]] = freq
            elif column_names[j] == '2FGM':
                if '2FGM' in master_dict[player_names[i]][curr_range]['Mid-Range']:
                    fgm = str(int(player_stats[i][j]) - int(master_dict[player_names[i]][curr_range]['Mid-Range'][column_names[j]]))
                    master_dict[player_names[i]][curr_range]['Layups'][column_names[j]] = fgm
                else:
                    fgm = str(int(player_stats[i][j]))
                    master_dict[player_names[i]][curr_range]['Layups'][column_names[j]] = fgm
            elif column_names[j] == '2FGA':
                if '2FGA' in master_dict[player_names[i]][curr_range]['Mid-Range']:
                    fga = str(int(player_stats[i][j]) - int(master_dict[player_names[i]][curr_range]['Mid-Range'][column_names[j]]))
                    master_dict[player_names[i]][curr_range]['Layups'][column_names[j]] = fga
                else:
                    fga = str(int(player_stats[i][j]))
                    master_dict[player_names[i]][curr_range]['Layups'][column_names[j]] = fga
            elif column_names[j] == '2FG%':
                if int(master_dict[player_names[i]][curr_range]['Layups']['2FGA']) != 0:
                    ha = float(master_dict[player_names[i]][curr_range]['Layups']['2FGM'])/float(master_dict[player_names[i]][curr_range]['Layups']['2FGA'])
                    ha = round(ha,1)
                    master_dict[player_names[i]][curr_range]['Layups'][column_names[j]] = str(ha) + "%"
                else:
                    master_dict[player_names[i]][curr_range]['Layups'][column_names[j]] = '-'



print(master_dict)
pickle.dump(master_dict, open("plus10_included.p", "wb"))
"""
print(efg_perc)
pickle.dump(efg_perc, open("efg_perc.p", "wb"))



"""
db = pandas.DataFrame({'player': player_names,
                       'team': [i[0] for i in player_stats],
                       'age': [i[1] for i in player_stats],
                       'gp': [i[2] for i in player_stats],
                       'g': [i[3] for i in player_stats],
                       'freq': [i[4] for i in player_stats],
                       'fgm': [i[5] for i in player_stats],
                       'fga': [i[6] for i in player_stats],
                       'fg%': [i[7] for i in player_stats],
                       'efg%': [i[8] for i in player_stats],
                       '2fg freq': [i[9] for i in player_stats],
                       '2fgm': [i[10] for i in player_stats],
                       '2fga': [i[11] for i in player_stats],
                       '2fg%': [i[12] for i in player_stats],
                       '3fg freq': [i[13] for i in player_stats],
                       '3pm': [i[14] for i in player_stats],
                       '3pa': [i[15] for i in player_stats],
                       '3p%': [i[16] for i in player_stats],
                       #'blk': [i[17] for i in player_stats],
                       #'tov': [i[18] for i in player_stats],
                       #'eff': [i[19] for i in player_stats]
                       }
                     )


db = db[['player',
         'team',
         'age',
         'gp',
         'g',
         'freq',
         'fgm',
         'fga',
         'fg%',
         'efg%',
         '2fg freq',
         '2fgm',
         '2fga',
         '2fg%',
         '3fg freq',
         '3pm',
         '3pa',
         '3p%'
         ]
      ]
"""
