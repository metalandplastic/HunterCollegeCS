#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/29/24
#A program that modifies the program from Lab 7 
import pandas as pd
import matplotlib.pyplot as plt

userInput = input("Enter name of input file: ")
userOutput = input("Enter name of output file: ")


homeless = pd.read_csv(userInput)
homeless["Fraction Children"] = homeless['Total Children in Shelter']/homeless["Total Individuals in Shelter"]
homeless.plot(x = "Date of Census", y =  "Fraction Children")

fig = plt.gcf()
fig.savefig(userOutput)