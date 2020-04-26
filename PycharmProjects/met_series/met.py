import pandas as pd
import matplotlib.pyplot as plt

pokemon_type = pd.read_csv(r"C:\Users\konga\Python_ds\pokemon.csv", squeeze=True, usecols=['Name', 'Type 1'], index_col='Name')
print(pokemon_type.value_counts())

pokemon_speed = pd.read_csv(r"C:\Users\konga\Python_ds\pokemon.csv", squeeze=True, usecols=['Name', 'Speed'], index_col='Name')
print(pokemon_speed.mean())

pokemon_type = pokemon_type.str.upper()
print(pokemon_type.head())

def change_type(type):
    if(type == 'DRAGON'):
        return 'FIRE'
    else:
        return type

pokemon_type = pokemon_type.apply(change_type)
print(pokemon_type.head())
print(pokemon_type.value_counts())

salary = pd.read_csv(r'C:\Users\konga\Python_ds\survey_results_public.csv', squeeze=True, usecols=['Salary'])
salary.dropna(inplace=True)
print(salary.head())
print(salary.count())

salary_increase = salary * 1.03
print(salary_increase.head())

survey = pd.read_csv(r'C:\Users\konga\Python_ds\survey_results_public.csv')
print(survey.columns.values)

developer_type = pd.read_csv(r'C:\Users\konga\Python_ds\survey_results_public.csv', usecols=['DeveloperType'], squeeze=True)
developer_type.dropna(inplace=True)
print(developer_type.head())

airport = pd.read_csv(r'C:\Users\konga\Python_ds\Air_Traffic_Passenger_Statistics.csv')
print(airport.columns.values)

region = pd.read_csv(r'C:\Users\konga\Python_ds\Air_Traffic_Passenger_Statistics.csv', usecols=['GEO Region'], squeeze=True)
print(region.value_counts())