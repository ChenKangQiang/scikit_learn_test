import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

data = pd.read_csv('../data/test.csv')
X = data[['speed', 'direction', 'distance']]
y = data[['tar']]
print(X)
print(data.head())
