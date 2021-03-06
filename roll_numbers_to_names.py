# -*- coding: utf-8 -*-
"""Roll-Numbers-to-Names.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/N-Shar-ma/Humanise-Data/blob/master/Roll_Numbers_to_Names.ipynb
"""

from google.colab import files

uploaded = files.upload()

import numpy as np
import pandas as pd
pd.options.display.max_columns = None

csai_df = pd.read_excel('csai.xlsx')
cs_df = pd.read_excel('cs.xlsx')
it_df = pd.read_excel('it.xlsx')

teams_df = pd.read_excel('oomprojectteams.xlsx')
teams_df.dropna(subset=teams_df.loc['member 1 rollno.':'member 4 roll number (optional)'].columns, how='all', inplace=True)
teams_df.reset_index(drop=True, inplace=True)
teams_df = teams_df.applymap(lambda x:str(x).upper().rstrip())

students_df = pd.concat([csai_df, cs_df, it_df])
students_df.reset_index(drop=True, inplace=True)
print(students_df)
print(teams_df)

def get_name_by_roll_no(roll_no):
  if (roll_no.startswith('L')) and (roll_no in students_df['Roll Number'].values):
    return students_df.loc[students_df['Roll Number']==roll_no]['Name'].item()
  else:
    return roll_no

# print(get_name_by_roll_no('LCS2020001'))

teams_df = teams_df.applymap(lambda x:get_name_by_roll_no(x))
print(teams_df)
teams_df.to_excel('humanisedteams.xlsx')
files.download('humanisedteams.xlsx')