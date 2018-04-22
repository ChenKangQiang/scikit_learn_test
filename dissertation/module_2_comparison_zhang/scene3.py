import numpy as np
import matplotlib.pyplot as plt

"""

恶意节点占比0.3，声誉0.1~0.9

"""
# plt.rcParams['font.sans-serif']=['SimHei']

# 用来显示中文，使用微软雅黑
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
y_ds = np.array([0.9938, 0.9937, 0.9969, 0.9927, 0.9946, 0.9968, 0.9979, 0.9992, 0.8931])
y_mv = np.array([0.995353, 0.998032, 0.99751, 0.992214, 0.990396, 0.997401, 0.995914, 0.993557, 0.99784])
y_wv = np.array([0.9969, 0.992, 0.9915, 0.9941, 0.9931, 0.9905, 0.9925, 0.9986, 0.9902])
y_bys = np.array([0.9976, 0.9962, 0.9961, 0.9998, 0.9993, 0.9969, 0.9947, 0.9321, 0.6012])

plt.plot(x, y_ds, label='D-S证据理论', marker='o')
plt.plot(x, y_mv, label='多数投票', marker='^')
plt.plot(x, y_wv, label='权重投票', marker='v')
plt.plot(x, y_bys, label='贝叶斯', marker='*')

plt.xlabel("恶意车辆平均声誉值")
plt.ylabel("TPR")

plt.yticks(np.linspace(0, 1, 6))

plt.legend()
plt.show()



