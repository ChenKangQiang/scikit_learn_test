from pandas import Series, DataFrame
import numpy as np
from datetime import datetime
import pandas as pd

df = DataFrame({'key1': ['a', 'b', 'b', 'b', 'a'],
                'key2': ['one', 'two', 'one', 'two', 'one'],
                'data1': np.random.randn(5),
                'data2': np.random.randn(5)})

grouped = df['data1'].groupby(df['key1'])

grouped.mean()

means = df['data1'].groupby([df['key1'], df['key2']]).mean()

states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])

for name, group in df.groupby('key1'):
    print(name)
    print(group)

for (k1, k2), group in df.groupby(['key1', 'key2']):
    print(k1, k2)
    print(group)

grouped2 = df.groupby(df.dtypes, axis=1)

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]

ts = Series(np.random.randn(6), index=dates)


dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000', '1/3/2000'])
dup_ts = Series(data=np.arange(5), index=dates)
dup_ts.index.is_unique



