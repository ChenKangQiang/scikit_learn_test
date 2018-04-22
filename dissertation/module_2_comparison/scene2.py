import numpy as np
import matplotlib.pyplot as plt

"""

恶意节点的平均声誉为0.7, 恶意节点占比0.1~0.9

"""
# 用来显示中文，使用微软雅黑
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
y_ds = np.array([0.9965, 0.9936, 0.9999, 0.9989, 0.9028, 0.299, 0.0749, 0.0038, 0.0])
y_mv = np.array([0.993401, 0.992829, 0.996835, 0.999505, 0, 0, 0, 0, 0])
y_wv = np.array([0.991, 0.9935, 0.9975, 0.9999, 0.661, 0.0003, 0.0, 0.0, 0.0])
y_bys = np.array([0.993, 0.9991, 0.978, 0.9468, 0.6042, 0.1848, 0.1946, 0.0401, 0.0])
# y_bys2 = np.array([0.9997, 0.9978, 0.9673, 0.8692, 0.3336, 0.3016, 0.0863, 0.0144, 0.001])
# y_bys3 = np.array([0.9997, 0.9925, 0.9766, 0.7111, 0.6188, 0.2438, 0.0929, 0.0023, 0.0002])

plt.plot(x, y_ds, label='D-S证据理论', marker='o')
plt.plot(x, y_mv, label='多数投票', marker='^')
plt.plot(x, y_wv, label='权重投票', marker='v')
plt.plot(x, y_bys, label='贝叶斯', marker='*')
# plt.plot(x, y_bys2, label='贝叶斯-0.85')
# plt.plot(x, y_bys3, label='贝叶斯-0.90')

plt.xlabel("恶意节点占比")
plt.ylabel("TPR")

plt.yticks(np.linspace(0, 1, 6))

plt.legend()
plt.show()



