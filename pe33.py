#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 4/3/24
#A program for organizing names

nameList = input('Please enter your list of names: ')
names = nameList.split('; ')

for name in names:
    lastName, firstName = name.split(', ')
    print(firstName, lastName)