import numpy as np
import matplotlib.pyplot as plt

"""

恶意节点占比0.7，声誉0.1~0.9
比较不同的先验概率的贝叶斯和证据理论

"""
# plt.rcParams['font.sans-serif']=['SimHei']
# 用来显示中文，使用微软雅黑
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
y_ds = np.array([0.9974, 0.9998, 0.9902, 0.6763, 0.5567, 0.2022, 0.0626, 0.013, 0.0001])
# y_mv = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
# y_wv = np.array([0.9903, 0.9672, 0.3051, 0.2331, 0.0, 0.0, 0.0, 0.0, 0.0])
y_bys = np.array([0.9907, 0.9945, 0.9927, 0.9931, 0.9951, 0.4596, 0.0568, 0.0145, 0.0001])
y_bys2 = np.array([0.9942, 0.9929, 0.9925, 0.9999, 0.7561, 0.5242, 0.061, 0.001, 0.0004])
y_bys3 = np.array([0.9998, 0.9931, 0.9925, 0.9884, 0.8932, 0.1135, 0.1148, 0.0028, 0.0])
y_bys4 = np.array([0.9992, 0.991, 0.9932, 0.9919, 0.6049, 0.17, 0.04, 0.0009, 0.0003])

plt.plot(x, y_ds, label='D-S证据理论', marker='o')
# plt.plot(x, y_mv, label='多数投票', marker='^')
# plt.plot(x, y_wv, label='权重投票', marker='v')
plt.plot(x, y_bys, label='贝叶斯-0.80', marker='*')
# plt.plot(x, y_bys2, label='贝叶斯-0.85')
# plt.plot(x, y_bys3, label='贝叶斯-0.90')
plt.plot(x, y_bys4, label='贝叶斯-0.95', marker='^')

plt.xlabel("恶意节点平均声誉值")
plt.ylabel("TPR")

plt.yticks(np.linspace(0, 1, 6))

plt.legend()
plt.show()



