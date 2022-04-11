# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:29:02 2022

@author: Mario
"""

import pandas as pd

pd.options.display.max_rows
pd.set_option('display.max_rows', None)


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

# company name text only
df['company_name'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

# state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[0])
print(df.job_state.value_counts())

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

# age of company
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)

# parsing of job description (python, ect)
df['python_yn'] = df['Job Description'].apply(lambda x: 'yes' if 'python' in x.lower() else 'no')
df['excel_yn'] = df['Job Description'].apply(lambda x: 'yes' if 'excel' in x.lower() else 'no')
df['R_yn'] = df['Job Description'].apply(lambda x: 'yes' if 'r studio' in x.lower() or 'r-studio' in x.lower() else 'no')
df['aws_yn'] = df['Job Description'].apply(lambda x: 'yes' if 'aws' in x.lower() else 'no')
df['spark_yn'] = df['Job Description'].apply(lambda x: 'yes' if 'spark' in x.lower() else 'no')

df_out = df.drop('Unnamed: 0', axis = 1)

df_out.to_csv('salary_data_cleaned.csv', index = False)

print(pd.read_csv('salary_data_cleaned.csv'))