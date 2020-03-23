import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rnd


week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
week_days_series = pd.Series(week_days)
print(week_days_series)

free_days = [False, False, False, False, False, True, True]
free_days_series = pd.Series(free_days)
print(free_days_series)

holidays = {'New Year': '01.01',
            'Christmas': '25.12'}
holidays_series = pd.Series(holidays)
print(holidays_series)

data_as_float_list = []
for i in range(100000):
    data_as_float_list.append(i*rnd.random())

data_as_float_list_series = pd.Series(data_as_float_list)
print('Size: ', data_as_float_list_series.size)
print('Bytes: ', data_as_float_list_series.nbytes)
print('Shape: ', data_as_float_list_series.shape)
print('Axes: ', data_as_float_list_series.axes)
print('Data type: ', data_as_float_list_series.dtype)
print('Index: ', data_as_float_list_series.index)
print('Is unique? : ', data_as_float_list_series.is_unique)
print('Is monotonic? : ', data_as_float_list_series.is_monotonic)

data_as_string_list = []
for i in range(100000):
    data_as_string_list.append(str(i*rnd.random()))

data_as_string_list_series = pd.Series(data_as_string_list)
print('Size: ', data_as_string_list_series.size)
print('Bytes: ', data_as_string_list_series.nbytes)
print('Data type: ', data_as_string_list_series.dtype)

cities = ['Shanghai', 'Beijing', 'Istanbul']
population = [24183300, 20794100, 15030000]

citypop = pd.Series(population, cities)
print(citypop)
print(citypop.sum())
print(citypop.mean())
print(citypop.index)
print(citypop.keys())
print(citypop.values)

age = ['do 6', '7 - 14', '15 - 17', '18 - 24', '25 - 39', '40 - 59', '60+']
num_of_accidents = [14, 334, 312, 5823, 9491, 7486, 4343]
incidents = pd.Series(num_of_accidents, age)
print(incidents)

print(incidents.where(incidents > 1000).dropna())
incidents1000 = incidents.where(incidents > 1000).dropna()
print(incidents1000)
print(incidents.filter(items=['18 - 24', '25 - 39']))
incidents.where(incidents <= 1000, inplace=True)
incidents.dropna(inplace=True)
print(incidents)