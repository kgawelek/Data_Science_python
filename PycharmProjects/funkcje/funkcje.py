from datetime import date
def PrintCat():
    print('''
    |\---/|
    | o_o |
     \_^_/
        ''')
    return
'''
PrintCat()
def daysToEndOfTheYear():
    from datetime import date
    from datetime import timedelta
    today = date.today()
    year = date.today().year
    endOfTheYear = date(year, 12, 31)
    daysDelta = endOfTheYear - today
    print('Do końca roku zostało', daysDelta.days, 'dni')
    return

daysToEndOfTheYear()
'''
def PrintAnimal(*animals):
    for animal in animals:
        if animal == 'cat':
            print(r'''
            |\---/|
            | o_o |
             \_^_/''')
            #return True
        elif animal == 'bear':
            print(r'''
            /  \.-"""-./  \
            \    -   -    /
             |   o   o   |
             \  .-'"'-.  /
              '-\__Y__/-'
                 `---`''')
            #return True
        elif animal == 'bat':
            print(r'''
               /\                 /\
              / \'._   (\_/)   _.'/ \
             /_.''._'--('.')--'_.''._\
             | \_ / `;=/ " \=;` \ _/ |
              \/ `\__|`\___/`|__/`  \/
                      \(/|\)/  
                 ''')
            #return True

        else:
            print("Cannot print", animal,". Correct values for the parameter are: cat, bear, bat")
            #return False

PrintAnimal('bat')
PrintAnimal('bear')
PrintAnimal('lion')
print(PrintAnimal('cat'))
print(PrintAnimal('dog'))

def DaysToEndOfTheYear(day = date.today().day,
                       month = date.today().month,
                       year = date.today().year):

    dateChecked = date(year, month, day)
    endOfTheYear = date(year, 12, 31)
    daysDelta = endOfTheYear - dateChecked

    #return daysDelta.days

DaysToEndOfTheYear(11, 8, 2019)
DaysToEndOfTheYear()
print(DaysToEndOfTheYear())

PrintAnimal('cat', 'bat')

def GiveGeomSeqElement(a1 = 2, q = 2, n = 2):
    if n < 1 or n != int(n):
        return "Error!"
    else:
        return a1*(q**(n-1))

print(GiveGeomSeqElement())
print(GiveGeomSeqElement(1, 2, 64))

for n in range(1, 11):
    print('a', n, '=', GiveGeomSeqElement(3, 2, n))
    n += 1

def GiveFactorForGeomSeq(term , nextTerm):
    factor = nextTerm/term
    return "Factor is:", factor

print(GiveFactorForGeomSeq(12, 24))

def GiveSumOfNElementsGeomSeq(a1 = 2, q = 2, n = 2):
    if q == 1:
        return 'The sum is:', a1*n
    else:
        return 'The sum is:', a1*((1-q**n)/(1-q))

print(GiveSumOfNElementsGeomSeq(2, 3, 4))
print(GiveSumOfNElementsGeomSeq(2, 1, 4))

def ZeroOfTheQuodraticFunction():
    print('Podaj parametry funkcji(a, b , c). Podaj je jako cyfry!')

    a_str = input('Podaj a:')
    b_str = input('Podaj b:')
    c_str = input('Podaj c:')
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)
    if a == 0 and b != 0:
        return ('To jest funckja liniowa, miejsce zerowe to:', (-c/b))
    elif a == 0 and b == 0:
        print('Ta funkcja nie ma miejsca zerowego')
    else:
        delta = b**2-4*a*c
        if delta < 0:
            print('Brak miejsc zerowych funckji')
        else:
            mz1 = (-b - delta**(1/2))/2*a
            mz2 = (-b + delta**(1/2))/2*a
            if mz1 == mz2:
                print('Wystepuje tylko jedno miejsce zerowe. Miejsce zerowe to:', mz1)
            else:
                print('Miejsca zerowe to:', mz1, mz2)

ZeroOfTheQuodraticFunction()