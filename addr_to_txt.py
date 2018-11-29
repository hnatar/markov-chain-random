#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('la_addr.csv')
for _, row in df.iterrows():
    """
    res = [row['UNIT'], row['NUMBER'], row['STREET'], row['CITY'], int(row['POSTCODE']) ]
    if str(res[0]) == 'nan':
        del res[0]
    res = list(map(str, res))
    res = ' '.join(res)
    """
    res = str(row['LAT'])+' , '+str(row['LON'])
    print(res)

