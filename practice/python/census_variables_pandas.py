import codecademylib3
from datetime import datetime

# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

#print first 5 rows
print(census.head())

# .dtypes on census data
#print(census.dtypes)

#print unique birth year values
print(census['birth_year'].unique())

#use .replace to change missing value and print unique vals
census['birth_year']= census['birth_year'].replace('missing', '1967')
print(census['birth_year'].unique())

#change birth year to sint
census['birth_year']= census['birth_year'].astype('int64')
print(census.dtypes)

#mean of birth year
print(census['birth_year'].mean())

#convert higher tax to category and print new order
census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered=True)

print(census['higher_tax'].unique())

#encode higher tx categories and get median
census['higher_tax'] = census['higher_tax'].cat.codes
print(census['higher_tax'].median())

#one-hot encode marital status and print new df head()
#census = pd.get_dummies(data=census, columns=['marital_status'])
#print(census.head())

#encode marital status variable
census['marital_codes'] = pd.Categorical(census['marital_status'], ['single', 'married', 'divorced', 'widowed'], ordered=True)

census['marital_codes'] = census['marital_codes'].cat.codes
print(census['marital_codes'])

census = pd.get_dummies(data=census, columns=['marital_status'])
print(census.head())

#create age group variable and then encode
age = datetime.now().year - census['birth_year']

bins = list(range(0, 121, 5)) + [float('inf')]
age_groups = [f"{i}-{i+4}" for i in range(0, 120, 5)] + ['120+']

census['age_group'] = pd.cut(age, bins=bins, labels=age_groups, right=True, include_lowest=True)

census['age_group'] = census['age_group'].cat.codes
print(census['age_group'])

census = pd.get_dummies(data=census, columns=['age_group'])
print(census.head())
