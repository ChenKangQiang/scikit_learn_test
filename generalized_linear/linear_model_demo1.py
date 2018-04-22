import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression

# read csv file directly from a URL and save the results
data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)

# first 5 rows
first5rows = data.head()
# last 5 rows
last5rows = data.tail()

print(first5rows)
print(last5rows)

# check the shape of the DataFrame(rows, colums)
print(data.shape)

# visualize the relationship between the features and the response using scatterplots
sns.pairplot(data, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales', size=7, aspect=0.8)

# 通过加入一个参数kind='reg'，seaborn可以添加一条最佳拟合直线和95%的置信带
sns.pairplot(data, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales', size=7, aspect=0.8, kind='reg')

plt.show()

####### 使用scikit_leran进行线性回归 #############

# create a python list of feature names
feature_cols = ['TV', 'Radio', 'Newspaper']

# use the list to select a subset of the original DataFrame
X = data[feature_cols]

# print the first 5 rows
# print(X.head())

# select a Series from the DataFrame
y = data['Sales']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


linreg = LinearRegression()

linreg.fit(X_train, y_train)

# 输出截距(偏移): b
print(linreg.intercept_)
# 输出系数
print(linreg.coef_)

# pair the feature names with the coefficients
# 在Python3中，zip、map、filter均返回迭代器
print(list(zip(feature_cols, linreg.coef_)))





