import os
import time
from builtins import list

'''
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))

dir = input('podaj katalog')

if os.path.isdir(dir):
    print('Katalog prawidłowy')
    file = input('podaj nazwe pliku')
    path = os.path.join(dir, file)
    if os.path.exists(path):
        print('Rozmiar:', os.path.getsize(path)/1000000, 'MB')
    else:
        print('Plik o podanej sciezce nie istnieje')
else:
    print('Podana sciezka nie jest sciezka katalogu')


file_path = r'c:\temp\data_input\orders.csv.txt'

with open(file_path, 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        order = line.split(',')
        if len(order) == 3:
            print('Apteka: %s, Lek: %s, ilość %s' % (order[0], order[1], order[2]))
        else:
            print('Dane nie poprawne')


file_path = input('Podaj ścieżke dostępu do pliku')
if os.path.exists(file_path):
    webaddresses = []
    line = input('Podaj adres www')
    while line != '':
        webaddresses.append(line)
        line = input('Podaj kolejny adres www')
else:
    'Sciezka nie prawidłowa, sprobuj ponownie'


file = open(file_path, 'w+')
for webaddress in webaddresses:
    file.write(webaddress + '\n')

file.close()

import sys
file_path = r'C:\temp\data_input\orders2.csv'

with open(file_path, 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        order = line.split(',')
        try:
            #order[2] = int(order[2])
            pharmacy = order[0]
            drug = order[1]
            amount = int(order[2])
            print('Apteka: %s, Lek: %s, Ilość: %d' % (pharmacy, drug, amount))
        except ValueError:
            print('Niepoprawnie podane dane,  liczba zamówionych leków powinna być podana jako'
                  'cyfra, a podanae zostało: %s' % order[2])
        except IndexError:
            print('Powinny zostać podane trzy wartości: nazwa apteki, nazwa leku, liczba zamówionych sztuk(jako cyfra')
            print('Ilość podanych danych: %d' % len(order))
        except:
            print('Wystąpił bład', sys.exc_info())
'''

line = input('Podaj cene kursu')
file_path = input('Podaj scieżke pliku')

with open(file_path, 'w+') as file:
    file.write('Cena kursu: %s' % line)