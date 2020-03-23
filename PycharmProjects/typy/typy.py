'''
percent = [2.606255012, 1.222935044, 1.283079391, 3.628708901, 6.856455493, 4.911788292,
           2.886928629, 0.781876504, 0.962309543, 2.265437049, 6.816359262, 3.688853248,
           3.468323978, 5.633520449, 4.530874098, 1.984763432, 0.922213312, 3.327987169,
           4.190056135, 5.493183641, 1.864474739, 10.60545309, 2.425821973, 2.726543705,
           8.740978348, 6.174819567]

countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal', 'United Kingdom', 'Serbia', 'Germany', 'Albania',
             'France', 'Czech Republic', 'Denmark', 'Australia', 'Finland', 'Bulgaria',
             'Moldova', 'Sweden', 'Hungary', 'Israel', 'Netherlands', 'Ireland',
             'Cyprus', 'Italy']
sumOfPoints = 4988
print(min(percent), '- minimum')

print(max(percent), '- maximum')

for i in range(0, len(countries)-1):
    print(percent[i])
    print(int(percent[i]))
    print(round(percent[i], 2))
    print('Ilość punktów:', round((percent[i]/100)*sumOfPoints))
    print(countries[i])
    print('\n')


import statistics
percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,

           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,

           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,

           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,

           8.740978348,6.174819567]
percent.sort()
print(percent)

print(statistics.median(percent))
print(statistics.median_high(percent), statistics.median_low(percent))
import math
degree = 360
radian = (degree/180)*math.pi
print(radian)
print(math.radians(degree))
small_pizza_r, big_pizza_r, family_pizza_r = 0.22, 0.27, 0.38
small_pizza_price, big_pizza_price, family_pizza_price = 11.50, 15.60, 22.00
small_pizza_area = (small_pizza_r**2)*math.pi
big_pizza_area = (big_pizza_r**2)*math.pi
family_pizza_area = (family_pizza_r**2)*math.pi
pricePerSquareMetre_small = small_pizza_price/small_pizza_area
pricePerSquareMetre_big = big_pizza_price/big_pizza_area
pricePerSquareMetre_family = family_pizza_price/family_pizza_area

print('Small: ', pricePerSquareMetre_small)
print('Big: ', pricePerSquareMetre_big)
print('Family: ', pricePerSquareMetre_family)

import random

for i in range (0,10):
    print('Random int number', i+1, 'is:', random.randint(1, 100))

number1 = random.randint(1, 100)
counter = 0

i = 0
while i >= 0:
    tmpRandomNR = random.randint(1, 100)
    counter += 1
    if tmpRandomNR == number1:
        print('Znaleziono number1, jest on rowny', tmpRandomNR)
        print('Liczba prób:', counter)
        break
    i+=1

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]
groupNumber = 0
i = 0
import random
random.shuffle(countries)
while i < len(countries):
    if i % 4 == 0:
        groupNumber += 1
        print('')
        print('Group', groupNumber)
    print(countries[i])
    i+=1

print(random.randint(1,6))
'''
poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''

'''
lines = poem.split('\n')
i1 = 0
i2 = 8

while i1 < 8 and i2 < 15:
    print(lines[i1], lines[i2])
    i1+=1
    i2+=1

import time

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

import calendar

print(calendar.month(2000, 7, 5, 2))
calendar.setfirstweekday(6)
print(calendar.month(2000, 7, 5, 2))
print(calendar.isleap(2000))

print(calendar.calendar(2019))


import math
import random
inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

inputdataLength = len(inputdata)
print(inputdataLength)
factortableLength = len(factortable)
print(factortableLength)


if inputdataLength == factortableLength:
    for i in range(0, inputdataLength):
        minValue = inputdata[i] - factortable[i]*inputdata[i]
        maxValue = inputdata[i] + factortable[i]*inputdata[i]
        minIntiger = math.floor(minValue)
        maxIntiger = math.ceil(maxValue)
        print('\n')
        print(i+1,':')
        print('Minimum value:', minValue)
        print('Maximum value:', maxValue)
        print('Minimum int:', minIntiger)
        print('Maximum int:', maxIntiger)
        print('--------------------')
else:
    print('inputdata and factortable need to have equal number of elements')


for i in range(0, inputdataLength):
    minValue = inputdata[i] - random.randint(0,1)*inputdata[i]
    maxValue = inputdata[i] + random.randint(0,1)*inputdata[i]
    minIntiger = math.floor(minValue)
    maxIntiger = math.ceil(maxValue)
    print('\n')
    print(i+1,':')
    print('Minimum value:', minValue)
    print('Maximum value:', maxValue)
    print('Minimum int:', minIntiger)
    print('Maximum int:', maxIntiger)
    print('--------------------')

import datetime

today = datetime.date.today()
print(today)
print(datetime.datetime.today().strftime("%d-%m-%Y"))

myNumbers = []

while len(myNumbers) < 7:
    newNumber = random.randint(1,49)
    if newNumber in myNumbers:
        print('eliminated')
        continue
    else:
        myNumbers.append(newNumber)
else:
    print('My lucky numbers are: ', myNumbers)
 '''
import random
colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']

allCards = []

for i in range(0,len(colors)):
    for j in range(0, len(figures)):
        card = colors[i] + figures[j]
        allCards.append(card)
print(allCards)

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

for i in range(0, len(allCards)):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

print(len(player1), player1)
print(len(player2), player2)

height = 7
width = 50
numbers = [1]
line = ''
for n in numbers:
    line += "%3d" % (n)
    print(line.center(width))
for _ in range(height - 1):

    newNumbers = [1]
    position = 0

    while position < len(numbers) -1:
        newNumbers.append(numbers[position]+numbers[position+1])
        position += 1

    newNumbers.append(1)
    numbers = newNumbers.copy()

    line = ''
    for n in numbers:
        line += "%3d" % (n)
        print(line.center(width))

