# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# Using the codes below, I found that the team with the smallest difference is Leicester and its difference is -34.

import os
import pandas as pd
import numpy as np

cwd = os.getcwd()
print cwd

os.chdir("/Users/xiangli/ds/metis/metisgh/prework/dsp/python")

football = pd.read_csv('/Users/xiangli/ds/metis/metisgh/prework/dsp/python/football.csv')

football.head()

football.info()

football['diff'] = football['Goals'] - football['Goals Allowed']

minima_r = np.min(football['diff'], axis=0)
print minima_r

num_row = len(football)
print num_row

def find_min(data):
    count = 0
    for e in data['diff']:
        if e != minima_r:
            count = count + 1
    return count
  
  find_min(football)
  
  print football['Team'][find_min(football)]
