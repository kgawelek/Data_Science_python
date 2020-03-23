from typing import List, Any, Union

likes = 550
shares = 80
minLikes = 500
minShares = 100
if likes < minLikes:
    print('Not enough likes to start a promotion')
elif shares < minShares:
    print('Not enough shares to start promotion')
else:
    print('Promotion has begun')

isPizzaOrdered = True
isBigBeverageOrdered = False
isWeekend = True

if not isWeekend and isPizzaOrdered or isBigBeverageOrdered:
    print('Dostałes kupon na burgera')
else:
    if isWeekend:
        print('Come back during work week')
    else:
        if not isPizzaOrdered and not isPizzaOrdered:
            print('To get a free burger you have to order a pizza or  big Drink')

diskSize = 500 #GB
diskUsed = 450
fileSize = 10

if fileSize <= (diskSize - diskUsed):
    print('File can be downloaded')
else:
    print('File is too big')

musclePain = False
fever = True
weakness = False
isMale = True
if musclePain and fever and weakness:
    print('suspiction of influenza')
else:
    print('The flu is unlikely')

if (musclePain and fever and weakness) or (isMale and (fever or weakness or musclePain)):
    print('suspiction of influenza')
elif weakness and not fever and not musclePain:
    print('Just take a rest!')
else:
    print('you may be cold')

isCheckCompleted = False

print('Check list is completed' if isCheckCompleted else print('Check lsit is not completed'))

firstRow = 1
lastRow = 31
currentRow = firstRow

while currentRow <= lastRow:
    print("Row ", currentRow)
    currentRow+=1

numbers: List[Union[int, Any]] = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i = 0
x = 0
z = 0
i2 = 0
x2 = 0

while i <= len(numbers):
    if numbers[x] == (numbers[i] ** 2):
        print('FOUND', numbers[i], numbers[x])
    x += 1
    if x==len(numbers):
        x=0
        i+=1

print('NASTEPNY PRZYKLAD')

while i2 <= len(numbers):
    if(numbers[i2]**2 == numbers[x2]) and (numbers[x2]**2 == numbers[z]):
        print('FOUND',numbers[i2], numbers[x2], numbers[z])
    z+= 1
    if 2 == len(numbers):
        z=0
        x2+=1
    if x2 == len(numbers):
        x2 = 0
        i2+=1