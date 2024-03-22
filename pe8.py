#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/17/24
#This program prompts the user to enter a phrase and then prints out the
#ASCII code of each character in the phrase.

user_string = input('Enter a phrase: ')
print('In ASCII:')
for c in user_string:
    print(ord(c))

