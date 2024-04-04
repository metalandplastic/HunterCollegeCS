#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/26/24
# This program computes the average and maximum population over time for a borough (entered by the user). This program assumes that the NYC historical population data file, nycHistPop.csv is in the same directory.

import pandas as pd

user_input = input('Enter borough: ')
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

print('Average population:',pop[user_input].mean())
print('Maximum Population:', pop[user_input].max())