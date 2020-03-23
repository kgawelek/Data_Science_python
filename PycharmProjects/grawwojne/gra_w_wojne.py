import random

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9} ]

allCards = []
for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)
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

print('Player 1:', player1)
print('Player 2:', player2)
# isGameFinished = len(player1) == 0 or len(player2) == 0
while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop()
    card2 = player2.pop()
    if card1['Power'] == card2['Power']:
        while card1['Power'] == card2['Power']:
            print('WAR')
            card1_1 = player1.pop()
            card2_2 = player2.pop()
            if len(player1) == 0 or len(player2) == 0:
                break
            card1 = player1.pop()
            card2 = player2.pop()



    if card1['Power'] > card2['Power']:
        player1.append(card1)
        player1.append(card2)
    else:
        player2.append(card1)
        player2.append(card2)
else:
    if len(player1) == 0:
        print('Player 2 won! He/she has', len(player2), 'cards')
    else:
        print('Player 1 won!He/she has', len(player1), 'cards')