
from sklearn import tree

# 输入样本
X = [[0, 0], [1, 1]]

# 划分标签
Y = [0, 1]

# 构造决策树类
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# 输入测试集进行测试
print(clf.predict([[2., 2.]]))
print(clf.predict([[0, 0]]))
print(clf.predict([[0, 0], [1, 1]]))
# 分类的概率预测
print(clf.predict_proba([[2., 2.]]))








