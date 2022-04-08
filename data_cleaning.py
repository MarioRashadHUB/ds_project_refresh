# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:29:02 2022

@author: Mario
"""

import pandas as pd

df = pd.read_csv('2022_ds_glassdoor_jobs.csv')

# salary parsing
# company name text only
# state field
# age of company
# parsing of job description (python, ect)

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1' ]
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K', '').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary','') )