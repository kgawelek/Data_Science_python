print('Hello World!')
print('its my first python code')
print('bell:  \a')
quote =('A good programmer is someone who always looks both ways before crossing a one-way street')
print(quote.upper())
print(quote.lower())
if quote.endswith('street'):
    print('true')

print(quote.replace('one', '1'))
music = ' "Universal Fanfare" Jerry Goldsmith \n"Happy Together" Garry Bonner \n"I\'m a Man" Steve Winwood'
print(music)
print('(\\(\\')
print('( -.- )')
print('O_(")(")')
somethingLikeNumber = '1000'
print(type(somethingLikeNumber))
article = '''
Monty Python (also collectively known as the Pythons)[2][3] are a British surreal comedy group who created the sketch comedy television show Monty Python's Flying Circus, which first aired on the BBC in 1969. Forty-five episodes were made over four series. The Python phenomenon developed from the television series into something larger in scope and impact, including touring stage shows, films, numerous albums, several books, and musicals. The Pythons' influence on comedy has been compared to the Beatles' influence on music.[4][5][6] Regarded as enduring icons of 1970s pop culture, their sketch show has been referred to as being “an important moment in the evolution of television comedy".[7]

Broadcast by the BBC between 1969 and 1974, Monty Python's Flying Circus was conceived, written, and performed by its members Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones, and Michael Palin. Loosely structured as a sketch show, but with an innovative stream-of-consciousness approach, aided by Gilliam's animation, it pushed the boundaries of what was acceptable in style and content.[8][9] A self-contained comedy team responsible for both writing and performing their work, the Pythons had creative control which allowed them to experiment with form and content, discarding rules of television comedy. Following their television work, they began making films, which include Monty Python and the Holy Grail (1975), Life of Brian (1979) and The Meaning of Life (1983). Their influence on British comedy has been apparent for years, while in North America, it has coloured the work of cult performers from the early editions of Saturday Night Live through to more recent absurdist trends in television comedy. "Pythonesque" has entered the English lexicon as a result.

In a 2005 poll of over 300 comics, comedy writers, producers and directors throughout the English-speaking world to find "The Comedian's Comedian", three of the six Pythons members were voted to be among the top 50 greatest comedians ever: Cleese at No. 2, Idle at No. 21, and Palin at No. 30.[10][11] 
'''
print(article.upper())
print(article.replace('Monty', 'flying'))
print(article.split(' '))

helloMessage = 'Hello %s!'
print(helloMessage % ('Kath'))
print(helloMessage % ('Ann'))

helloMessage2 = 'Hello {0:s}'
print(helloMessage2.format('Kath'))

helloMessage3 = ('%s has %d %s')
print(helloMessage3 % ('Kate', 1, 'animal'))
print(helloMessage3 % ('Ann', 1000, '$'))

line = ('%20s costs %6d€')
print(line % ('ICE CREAM', 3))
print(line % ('CHIPS', 4))
print(line % ('COOKIES', 5))
print(type(line))

name = 'Konrad'
age = 19
daysInYear = 365

message = '%s is %d years old, and it\'s about %d days'
print(message % (name, age, age*daysInYear))

message2 = '{0:s} is {1:d} years old, and it\'s about {2:d} days'
print(message2.format(name, age, age*daysInYear))
print('1234567890 divided by 12345 is', 1234567890//12345, 'and the rest is', 1234567890%12345)