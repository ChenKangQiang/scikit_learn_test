import numpy as np
import matplotlib.pyplot as plt

"""

恶意节点的平均声誉为0.4, 恶意节点占比0.1~0.9

"""
# 用来显示中文，使用微软雅黑
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
y_ds = np.array([0.9919, 0.9955, 0.9967, 0.9922, 0.9961, 0.999, 0.8761, 0.1104, 0.0329])
y_mv = np.array([0.995388, 0.995368, 0.998667, 0.997769, 0, 0, 0, 0, 0])
y_wv = np.array([0.9916, 0.9987, 0.9952, 0.993, 0.9942, 0.9273, 0.0408, 0.0, 0.0])
y_bys = np.array([0.9901, 0.9923, 0.9912, 0.9917, 0.9904, 0.9934, 0.9984, 0.9988, 0.9614])

plt.plot(x, y_ds, label='D-S证据理论', marker='o')
plt.plot(x, y_mv, label='多数投票', marker='^')
plt.plot(x, y_wv, label='权重投票', marker='v')
plt.plot(x, y_bys, label='贝叶斯', marker='*')

plt.xlabel("恶意节点占比")
plt.ylabel("TPR")

plt.yticks(np.linspace(0, 1, 6))

plt.legend()
plt.show()



