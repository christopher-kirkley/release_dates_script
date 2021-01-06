import numpy as np
import pandas as pd

release_date = input('Choose a release date DD/MM/YY: ')

df = pd.read_csv('release_dates.csv', index_col='Release Date')

try:
    dates_df = df.loc[release_date]
    dates = dates_df.to_dict()

    for key, value in dates.items():
        print(f'{key}: {value}')
except KeyError:
    print('Invalid date')

# check that is not empty

def write_to_emacs(dates):
    with open('testproj.org', 'a') as f:
        f.write('\n* TIMELINE\n')
        for item, date in dates.items():
            f.write(f'** TODO {item}\n')
            f.write(f'  DEADLINE: <2021-05-21 Tue>\n')
        
write_to_emacs(dates)
