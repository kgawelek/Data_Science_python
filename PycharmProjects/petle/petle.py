'''
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i = 0
x = 0
z = 0

while i <= len(numbers):
    if numbers[i]**2 == numbers[x] and numbers[x]**2 == numbers[z]:
        print('FOUND',numbers[i], numbers[x], numbers[z])

    z+= 1

    if z == len(numbers):
        z=0
        x+=1

    if x == len(numbers):
        x = 0
        i+=1

cargo = [40, 40, 45, 3, 4, 35, 24, 31, 8, 19, 10, 13, 2, 3, 4, 2]
print(sum(cargo))
i2 = 0
box = []
box2 = []
box3 = []
box4 = []
boxCapacity = 90

while i2 <= len(cargo)-1:
    if sum(box) < boxCapacity:
        box.append(cargo[i2])
    if sum(box) > boxCapacity:
        box.remove(cargo[i2])
        box2.append(cargo[i2])
        if sum(box2) > boxCapacity:
            box2.remove(cargo[i2])
            box3.append(cargo[i2])
            if sum(box3) > boxCapacity:
                box3.remove(cargo[i2])
                box4.append(cargo[i2])
    i2+=1
    print('Sklad box1:', box, 'waga box1:', sum(box))
    print('Sklad box2:', box2, 'waga box2:', sum(box2))
    print('Sklad box3:', box3, 'waga box3:', sum(box3))
    print('Sklad box4:', box4, 'waga box4:', sum(box4))
    print('')

number = 0
nextNumber = 1

while nextNumber<=50:
    print(number,'+',nextNumber,'=',number+nextNumber)
    number+=1
    nextNumber+=1

import random
from typing import List

randomNumber = random.randint(0, 20)

guess = -1

while guess != randomNumber:
    print('Zgadnij liczbe od 0 do 20')
    guess = int(input())

    if guess == randomNumber:
        print('ZGADLES')
    elif randomNumber > guess:
        print('Ta liczba jest wieksza od ', guess)
    elif randomNumber < guess:
        print('Ta liczba jest mniejsza od ', guess)

data = ['Error:File cannot be open',
            'Error:No free space on disk',
            'Error:File missing',
            'Warning:Internet connection lost',
            'Error:Access denied']
for errors in data:
    print(errors.upper())

for errors in data:
    elements = errors.split(':')
    if elements[0] == 'Error':
        print(elements[1].upper())
    else:
        print(elements[1])

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for number in range(10):
    print(string_A)
print('')
for number in range(9):
    if number % 2 == 0:
        print(string_A)
    else:
        print(string_B)

for number in range(1, 10):
    if number % 2 == 0:
        print('x'*number)
    else:
        print('o'*number)

i = 10
result = 1
while i > 0:
    result = i*result
    i-=1
else:
    print('10!= ', result)
factorial = 1
x=10
for number in range(1,x+1):
    results = 1
    for j in range(1, number+1):
        results *= j
    print(number,'! = ',results)
'''
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']
'''
for noun in range(0, len(list_noun)+1):
    tmpNoun = list_noun[noun]
    for adj in range(0, len(list_adj)+1):
        tmpAdj = list_adj[adj]
        print(tmpAdj, tmpNoun)

i = 0
j = 0
while i <= len(list_noun)+1:
    while j <= len(list_adj)+1:
        print(list_adj[j]+' '+list_noun[i])
        j+=1
    i+=1


for noun in list_noun:
    for adj in list_adj:
        print(adj+' '+noun)

for candidate in range(2, 31):
    for divider in range(2, candidate):
        if candidate % divider == 0:
            print(candidate, ' is not a prime number, its divided by ', divider)
            break
    else:
            print(candidate, ' is prime')


text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'
words = text.split(' ')

shortText = ''
counter = 0
for word in words:
    shortText += word + ' '
    counter += 1
    if counter >= 20:
        break
print(shortText)

definitions = [
    'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
    'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
    'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
    'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.'
]


for definition in definitions:
    words = definition.split(' ')
    shortText = ' '
    counter = 0
    for word in words:
        shortText += word + ' '
        counter += 1
        if counter >= 20:
            print(shortText)
            break
'''

menu = '''
Choose what you want me to do for you:
1 - COFFEE
2 - TEA
3 - MAKE ME SMILE
---------------
To stop this script select 0
'''

smile = '''

                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""""

isOpen = True
chosenOption = 0
while isOpen:
    print(menu)
    print('Please choose an option')
    chosenOption = int(input())
    if chosenOption == 1:
        print('Function COFFEE not implemented')
        input('Press enter')
        continue
    if chosenOption == 2:
        print('Function TEA not implemented')
        input('Press enter')
        continue
    if chosenOption == 3:
        print(smile)
        input('Press enter')
        continue
    if chosenOption == 0:
        break


initialCapital = 20000
maxYears = 10
i = 0
percent = 0.03
while i < maxYears:
    initialCapital += initialCapital * percent
    i+=1
else:
    print('Your savings: ', initialCapital)

number = 20730906
sumOfDigits = 0
tmpNumber = number
while tmpNumber > 0:
    digit = tmpNumber % 10
    sumOfDigits += digit
    tmpNumber = tmpNumber//10
else:
    print(sumOfDigits)
 

text =  ''United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.''

words = text.split(' ')
wordsTab = []

for word in words:
    wordsTab.append(word)
print(wordsTab)
shortWords = []

i = 0
while i < len(wordsTab):
    if len(wordsTab[i]) <= 6:
        shortWords.append(wordsTab[i])
    i+=1
print(shortWords)

fibonacciIterations = 20
i = 0
j = 0
for i in range(0,fibonacciIterations):
    j = i+1
    fibonacciNumber = i + j
    print(fibonacciNumber)
'''

text = '''Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.'''

textTab = []

tmpText = text.split(' ')

for word in tmpText:
    textTab.append(word)
print(textTab)
pTab = []
for word in textTab:
    if word.count('p') >= 1:
        pTab.append(word)
print(pTab)
dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'}
for word in dictionary.keys():
    print(word,'-', dictionary[word])
