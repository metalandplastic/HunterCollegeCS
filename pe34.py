#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 4/02/24
#A program that asks the user for the hour of the day (in 24 hour time), and prints a response based on constraints 

userInput = int(input('Enter hour of day (in 24 time): '))
if userInput <= 11:
    print('Good Morning'),
elif userInput >12 and userInput <=16:
    print('Good Afternoon'),
else: 
    print('Good Evening')


