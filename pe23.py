#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/20/24
#A program that asks the user for a list of nouns (separated by spaces) and approximates the fraction that are plural by counting the fraction that end in "s"

user_input = input("Enter List of Nouns (separated by spaces): ")
  
num_words = user_input.count(' ') + 1

num_plural = user_input[:-1].count('s ')

if user_input.endswith('s'):
        num_plural += 1

if num_words > 0:
        plural_fraction = num_plural / num_words
else:
        plural_fraction = 0
        
plural_fraction = round(plural_fraction, 1)


print("Number of words: ", num_words)
print("Fraction of your list that is plural is ", plural_fraction)
