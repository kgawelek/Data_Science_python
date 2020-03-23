import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math
import random as rnd


'''
t = np.arange(0., 5., 0.2)
wykres = plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show(wykres)

days = [1, 2, 3, 4, 5]
amount = [1,5,20,450,700]

wykres2 = plt.plot(days, amount, 'bo')
plt.show(wykres2)

months = np.arange(1, 13, 1)
print(months)
income = 100 + 3*months
print(income)
cost = 50 + 10*months

plt.plot(months, income, 'go', months, cost, 'r^')
plt.show()

x = np.arange(-5, 5.1, 0.1)
plt.plot(x, 2**x)
plt.show()


weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekDaysSeries = pd.Series(weekDays)
print(weekDaysSeries)

freeDays = [False, False, False, False, False, True, True]
freeDaysSeries = pd.Series(freeDays)
print(freeDaysSeries)

holidays = {'New Year': '2018.01.01',
            'Epiphany': '2018.01.06',
            'Easter': '2018.04.01'}
holidaysSeries = pd.Series(holidays)
print(holidaysSeries)

tab1 = []
tab2 = []

def przepisz (tab, tabx):
    tab = list(input("Podaj liczby należace do tablicy"))
    n = len(tab)-1
    while n >= 0:
        tabx.append(tab[n])
        n -= 1
    else:
        print(tabx)


przepisz(tab1, tab2)


dataAsFloatList = []
for i in range(100000):
    dataAsFloatList.append(i*rnd.random())

dataAsFloatSeries = pd.Series(dataAsFloatList)
print("Size:", dataAsFloatSeries.size)
print("Bytes:", dataAsFloatSeries.nbytes)
print("Shape:", dataAsFloatSeries.shape)
print("Axes:", dataAsFloatSeries.axes)
print("Data type:", dataAsFloatSeries.dtype)
print("Index:", dataAsFloatSeries.index)
dataAsFloatSeries_sorted = dataAsFloatSeries.sort_values()
print("Is unique", dataAsFloatSeries.is_unique)
print("Is monotonic", dataAsFloatSeries.is_monotonic)
print("Is monotonic", dataAsFloatSeries_sorted.is_monotonic_increasing)
'''
cities = ["Shanghai", "Beijing", "Istanbul"]
population = [24183300, 20794100, 15030000]
citypop = pd.Series(population, cities)
print(citypop)
citypop = pd.Series(index = cities, data = population)
print(citypop)
print("Srednia il. mieszk.", citypop.mean())
print('Suma', citypop.sum())
print(citypop.index, citypop.keys())
print(citypop.values, citypop.get_values())
plt.plot(cities, population, 'o')
plt.show()
ages = [ '6', '7-14', '15-17', '18-24', '25-39', '40-59', '60 i wiecej']
numbersOfAccidents = [ 14
,334,312,5823,9491,7486,4343]

incidents = pd.Series(index=ages, data=numbersOfAccidents)
print(incidents)
print(incidents.where(incidents > 1000))
incidents1000 = incidents.where(incidents > 1000).dropna()
print(incidents1000)
print(incidents)
print(incidents.filter(items=['18-24', '25-39', '40-59']))
incidents.where(incidents <= 1000, inplace=True)
incidents.dropna(inplace=True)
print(incidents)

namesList =  ['Albania','Austria','Belarus',
'Belgium','Bulgaria','Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia',
'Finland', 'France', 'Germany','Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy',
'Latvia', 'Lithuania', 'Luxembourg', 'Macedonia', 'Malta', 'Montenegro', 'Netherlands',
'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovenia', 'Spain', 'Sweden','Switzerland','United Kingdom','Turkey','Ukraine']

energy2010list = [1947, 8347, 3564, 8369,4560,3814,4623,6348,6328,6506,16483,7736,7264,5318,3876,
51440,5911, 5494,3230,3471,16830,3521,4171,5420,7010,24891,3797,4959,2551,
6410,4359,6521,5707,14934,8175,2498,3550,5701]

energy2012list = [2118,8507,3698,7987,4762,3819,4057,6305,6039,6689,15687,7344,7270,5511,3919,
53203,5665,5398,3588,3608,14696,3626,4761,5416,6871,23658,3899,4736,2604,
6617,4387,6778,5573,14290,7886,2794,3641,5452]

namesSeries = pd.Series(namesList)
energy2010Series = pd.Series(energy2010list)
energy2012Series = pd.Series(energy2012list)

mean2010 = energy2010Series.mean()
mean2012 = energy2012Series.mean()
print(mean2010)
print(mean2012)

#filterAboveMean2010 = energy2010Series.where(energy2010Series > mean2010).dropna()
filterAboveMean2010 = energy2010Series > mean2010
print(filterAboveMean2010)

filterAboveMean2012 = energy2012Series > mean2012
print(namesSeries.where(filterAboveMean2010 & filterAboveMean2012).dropna())

allInfo = pd.read_csv('C:/temp/data_input/survey_results_public.csv')
education = pd.read_csv('C:/temp/data_input/survey_results_public.csv', usecols=['EdLevel'])
print(education.head(5))
print(type(education))
education = pd.read_csv('C:/temp/data_input/survey_results_public.csv', usecols=['EdLevel'], squeeze=True)
print(type(education))
print(education.tail(10))
country = allInfo['Country']
print(country)
print(type(country))
filterUSA = country == "United States"
print(filterUSA.head(5))
print(education.where(filterUSA).dropna().head(10))


