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
