import numpy as np
import matplotlib.pyplot as plt

"""

恶意节点占比0.3， 攻击者的声誉值0.1~0.9

"""
# 用来显示中文，使用微软雅黑
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
y_svm = np.array([0.966551,  0.966100, 0.960790, 0.958528, 0.950790, 0.956747, 0.962896, 0.960356, 0.96356])
y_mv = np.array([0.990745, 0.995455, 0.994051, 0.995104, 0.998863, 0.995248, 0.990223, 0.992851, 0.994824])
y_wv = np.array([0.9943, 0.9919, 0.9943, 0.9955, 0.991, 0.9924, 0.9974, 0.9922, 0.9934])
y_bys = np.array([0.9993, 0.9931, 0.9971, 0.9923, 0.9975, 0.9902, 0.993, 0.9735, 0.0986])

plt.plot(x, y_svm, label='SVM', marker='o')
plt.plot(x, y_mv, label='多数投票', marker='^')
plt.plot(x, y_wv, label='权重投票', marker='v')
plt.plot(x, y_bys, label='贝叶斯', marker='*')

plt.xlabel("恶意节点平均声誉值")
plt.ylabel("TPR")

plt.yticks(np.linspace(0, 1, 6))

plt.legend()
plt.show()



