import numpy as np
import pandas as pd
from pandas import DataFrame

frame = DataFrame(data=np.random.randn(4, 5))
print(frame)

df1 = DataFrame(np.arange(9).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = DataFrame(np.arange(12).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1)
print(df2)

df3 = df1 + df2
print(df3)

