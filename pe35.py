#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 4/4/24
#A program that modifies the ticket.csv search from lab 8 for user inputs

import pandas as pd

csvFile = input('Enter CSV file name: ')    #Name of the CSV file
column = input('Enter attribute: ')
tickets = pd.read_csv(csvFile)     #Read in the file to a dataframe
print('The 10 worst offenders are:')
print(tickets[column].value_counts()[:10]) #Print out the dataframe			#Print out the dataframe
