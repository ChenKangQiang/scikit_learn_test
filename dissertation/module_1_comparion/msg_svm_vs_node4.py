import numpy as np
import matplotlib.pyplot as plt

"""

恶意节点占比0.6， 攻击者的声誉值0.1~0.9

"""
# 用来显示中文，使用微软雅黑
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
y_svm = np.array([0.966551,  0.966100, 0.960790, 0.958528, 0.950790, 0.956747, 0.962896, 0.960356, 0.96356])
y_mv = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
y_wv = np.array([0.996, 0.9981, 0.8434, 0.0266, 0.0, 0.0, 0.0, 0.0, 0.0])
y_bys = np.array([0.999, 0.9962, 0.9995, 0.9953, 0.9923, 0.6954, 0.0486, 0.0, 0.0])

plt.plot(x, y_svm, label='SVM', marker='o')
plt.plot(x, y_mv, label='多数投票', marker='^')
plt.plot(x, y_wv, label='权重投票', marker='v')
plt.plot(x, y_bys, label='贝叶斯', marker='*')

plt.xlabel("恶意节点平均声誉值")
plt.ylabel("TPR")

plt.yticks(np.linspace(0, 1, 6))

plt.legend()
plt.show()



