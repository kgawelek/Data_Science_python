import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rnd

'''
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
#print(citypop)
#print(citypop.sum())
#print(citypop.mean())
#print(citypop.index)
#print(citypop.keys())
#print(citypop.values)

age = ['do 6', '7 - 14', '15 - 17', '18 - 24', '25 - 39', '40 - 59', '60+']
num_of_accidents = [14, 334, 312, 5823, 9491, 7486, 4343]
incidents = pd.Series(num_of_accidents, age)
#print(incidents)

#print(incidents.where(incidents > 1000).dropna())
incidents1000 = incidents.where(incidents > 1000).dropna()
#print(incidents1000)
#print(incidents.filter(items=['18 - 24', '25 - 39']))
incidents.where(incidents <= 1000, inplace=True)
incidents.dropna(inplace=True)
#print(incidents)

names_list =['Albania', 'Austria', 'Belarus', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France',
             'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy',
             'Latvia', 'Lithuania', 'Luxembourg', 'Macedonia', 'Malta', 'Montenegro', 'Netherlands',
             'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovenia', 'Spain',
             'Sweden', 'Switzerland', 'United Kingdom', 'Turkey', 'Ukraine']

energy_list2010 = [1947,8347,3564,8369,4560,3814,4623,6348,6328,6506,16483,7736,7264,5318,3876,
51440,5911,5494,3230,3471,16830,3521,4171,5420,7010,24891,3797,4959,2551,
6410,4359,6521,5707,14934,8175,2498,3550,5701]

energy_list2012 = [2118,8507,3698,7987,4762,3819,4057,6305,6039,6689,15687,7344,7270,5511,3919,
53203,5665,5398,3588,3608,14696,3626,4761,5416,6871,23658,3899,4736,2604,
6617,4387,6778,5573,14290,7886,2794,3641,5452]

names_series = pd.Series(names_list)
energy_2010_series = pd.Series(energy_list2010)
energy_2012_series = pd.Series(energy_list2012)

mean2010 = energy_2010_series.mean()
mean2012 = energy_2012_series.mean()

#print(mean2010, ' ', mean2012)

filter_above_mean2010 = energy_2010_series > mean2010
filter_above_mean2012 = energy_2012_series > mean2012

#print(names_series.where(filter_above_mean2010 & filter_above_mean2012).dropna())

education = pd.read_csv("survey_results_public.csv", usecols=['FormalEducation'])

education = pd.read_csv("survey_results_public.csv", usecols=['FormalEducation'], squeeze=True)


all_info = pd.read_csv("survey_results_public.csv")
country = all_info['Country']
#print(type(country))
filter_USA = country == 'United States'
#print(filter_USA.head())

#print(education.where(filter_USA).dropna().head())


salary = pd.read_csv("survey_results_public.csv", usecols=["Salary"], squeeze=True)
salary.dropna(inplace=True)
#print(salary.head())
#print(len(salary))
#print(min(salary), '  ', max(salary))
#print(list(salary))
#print(dict(salary))
list_salary_sorted = sorted(list(salary))
#print(list_salary_sorted[:5])
salary.name = "Salary of a person"
#print(salary.name)

salary = pd.read_csv("survey_results_public.csv", usecols=["Salary"], squeeze=True)
#print(salary.sort_values(ascending=False).head())
salary.sort_values(ascending=False, inplace=True)
#print(salary.head())
#print(salary.sort_index(ascending=False).head())

max_salary = salary.sort_values(ascending=False).head(100)
min_salary = salary.sort_values().head(100)
#print("Max salary mean = ", max_salary.mean())
#print("Min salary mean = ", min_salary.mean())



countries = pd.read_csv("survey_results_public.csv", usecols=["Country"], squeeze=True)
countries.dropna(inplace=True)
#print(countries.head())
#print('Poland' in countries.values)
#print(countries.count())
company_size = pd.read_csv("survey_results_public.csv", usecols=["CompanySize"], squeeze=True)
company_size.dropna(inplace=True)
company_size.sort_values(inplace=True)
company_size.reset_index(drop=True, inplace=True)
#print(company_size.head())
'''
country_symbols = ['PL', 'ES', 'FR', 'IT', 'FI', 'SE', 'NO']
country_names = ['Poland', 'Spain', 'France', 'Italy', 'Finland', 'Sweden', 'Norway']
country_series = pd.Series(country_names, country_symbols)
print(country_series.iloc[1])
nordic = ['FI', 'SE', 'NO']
print(country_series[nordic])
to_find = ['PL', 'ES', 'EN']
print(country_series.reindex(to_find))
print(country_series.loc[country_series.index.intersection(to_find)])
