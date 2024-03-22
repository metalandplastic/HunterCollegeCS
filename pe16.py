#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/7/24
#A program that slices through a string and prints each step forward and then reversed.

s = input("enter a string: ")

ls = len(s)

for i in range(ls):
    print(s[:i])
for i in range(ls):
    print(s[i:])
    
print("Thank you for using my program!")
