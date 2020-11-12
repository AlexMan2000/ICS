year = int(input('Please enter a year number'))
while year < 0:
    year = int(input('Please enter an AC year'))
#Corresponding zodiac starts from the year number that can be divided by 12 (e.g. 2004 // 12 = 167 , 'Monkey').
zodiac_list = ['Monkey','Rooster','Dog','Pig','Rat','Ox','Tiger','Hare','Dragon','Snake','Horse','Sheep']
print('Year {0} is the year of {1}'.format(year,zodiac_list[year%12]))
