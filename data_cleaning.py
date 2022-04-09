# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:29:02 2022

@author: Mario
"""

import pandas as pd

df = pd.read_csv('2022_ds_glassdoor_jobs.csv')

# company name text only
# state field
# age of company
# parsing of job description (python, ect)

# salary parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1' ]
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K', '').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary',''))

df['min_salary'] = min_hr.apply(lambda x: (x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: (x.split('-')[1]))

df['fixed_min_salary'] = df['min_salary'].apply(lambda x: x.replace(':', ''))

df = df.astype({'fixed_min_salary':'int', 'max_salary':'int'})

df['avg_salary'] = (df.fixed_min_salary+df.max_salary)/2

# test from linux PC

# company name text only
# state field
# age of company
# parsing of job description (python, ect)