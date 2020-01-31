# -*- coding: utf-8 -*-
"""GMlab4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U7NDbGOz0Ac7HA6J4qDepaMCO7u4HbPc
"""

# Commented out IPython magic to ensure Python compatibility.
# %pylab inline

import pandas as pd

"""## Task 1

#### Create a dataframe from a numpy random int array of shape (10, 5). Name the columns as 'A'-'E'.
"""

df = pd.DataFrame(np.random.randint(0, 10, (10, 5)), columns=['A', 'B', 'C', 'D', 'E'])
df

"""#### Calculate mean, max, min for each column"""

print(df.mean())
print(df.max())
print(df.min())

"""#### Make a new dataframe by substracting mean from each of the columns in the above dataframe"""

df2 = df.transform(lambda x: x - x.mean())
#df2 = df - df.mean()
df2

"""#### Make a new dataframe from the orginal dataframe such that the numbers in the first column is squared."""

df3 = df.copy()
df3['A'] = df3['A']**2
df3

"""## Task 2

### Fill the NaN values in the following dataframe with zero
"""

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
df

df = df.fillna(0)
df

"""## Task 3"""

from google.colab import files
uploaded = files.upload()

import io
births_data = pd.read_csv(io.BytesIO(uploaded['births.csv']))

births.head(10)
print(births.head(10))
#births.describe()

"""#### Generate a dataframe for birth data between year 1970 and 1980"""

b2 = births[(births['year']>=1970) & (births['year']<=1980)]
b2.head(10)

"""#### Use the dataframe generated above and ``groupby`` to show total birth for male and female between year 1970 and 1980"""

b2.groupby('gender')['births'].sum()

"""#### and average daily birth"""

b2.groupby('gender')['births'].mean()

"""#### Based on the datafrome generated above, make a pivot table showing total birth for month and gender (i.e., your table should have 12 rows corresponding to Jan-Dec and 2 columns corresponding to F and M. Each cell should be the total births in that month across the years for F and M.)"""

bp = b2.pivot_table('births', index='month', columns='gender', aggfunc='sum')
bp

"""#### Plot the above table as two curves: one for F and one for M. x_axis should be month and label the y_axis as 'Total Births'"""

bp.plot()
ylabel('total births');

"""#### In the original table, find the max number of births of boys on a single day and the date that gives the max number."""

mm = births[births['gender']=='M']['births'].max()
print(mm)
births[births['births'] == mm]

