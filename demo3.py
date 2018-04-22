import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams['font.sans-serif']=['SimHei']

plt.rcParams['font.sans-serif']=['Microsoft YaHei'] #用来显示中文，使用微软雅黑
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x = np.linspace(100, 1000, 10)
y_svm = np.array([0.971, 0.964, 0.959, 0.954, 0.950, 0.951, 0.948, 0.945, 0.940, 0.937])
y_bpnn = np.array([0.955, 0.952, 0.948, 0.942, 0.941, 0.940, 0.935, 0.932, 0.929, 0.929])

plt.plot(x, y_svm, label='SVM', marker='o')
plt.plot(x, y_bpnn, label='BPNN', marker='^')

plt.xlabel("消息数量")
plt.ylabel("TPR")

plt.xticks(np.linspace(100, 1000, 10))
plt.yticks(np.linspace(0.93, 0.98, 6))

plt.legend()

plt.show()

