import pandas as pd
from pandas import Series

obj1 = Series(range(3), index=['a', 'b', 'c'])
index = obj1.index
values = obj1.values

print(obj1)
print(index)
print(values)

# 重新索引
obj2 = obj1.reindex(index=['a', 'b', 'c', 'd', 'e'], fill_value=0)
print(obj2)

