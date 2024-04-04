#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/4/24
#A program that asks the user for a borough from csv file, and name for the output file, then displays the fraction of the population that has lived in that borough, over time. Uses pandas and matplotlib

import matplotlib.pyplot as plt
import pandas as pd

# user_input = input("Enter borough name: ")
# user_file = input("Enter output file name: ")
pop = pd.read_csv('nycHistPop.csv',skiprows=5)
pop["Fraction"] = pop[user_input]/pop["Total"]
pop.plot(x="Year",y="Fraction")

fig = plt.gcf()
fig.savefig(user_file)


plt.show()

