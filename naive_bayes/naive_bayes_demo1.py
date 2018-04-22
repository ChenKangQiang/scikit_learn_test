from sklearn import datasets
from sklearn.naive_bayes import GaussianNB

iris = datasets.load_iris()
# 数据集的属性
print(iris.data)
# 数据集的结果
print(iris.target)

# 高斯朴素贝叶斯分布
gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
print("Number of mislabeled points out of a total %d points : %d"
      % (iris.data.shape[0], (iris.target != y_pred).sum()))
