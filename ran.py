def getYear():
    year = int(input('Enter a year:' ))
    while year <= 2000 or year >= 2021:
        print('Please enter a valid year: ')
        year = int(input('Please enter a year:' ))
    print('You entered the year:', year)
    
test = getYear()
