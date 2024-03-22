#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/11/24
# This program tells you how long until the weekend, days/hours, based on user input of hours.

hours = int(input("How many hours until the weekend: "))

days = hours // 24

leftovers = hours % 24

if days == 0 and leftovers == 0:
	print("Its the weekend!")
elif days != 0 or leftovers != 0:
	print("Days:",days)
	print("Hours:", leftovers)
