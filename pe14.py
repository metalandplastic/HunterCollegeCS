#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/7/24
#This program reverses a string and prints it twice, 1 char per line in reverse.

message = input("Enter a message: ")

reversed_message = message[::-1]

for c in reversed_message:
    print(c, c)

 