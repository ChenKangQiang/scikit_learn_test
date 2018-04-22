import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams['font.sans-serif']=['SimHei']

plt.rcParams['font.sans-serif']=['Microsoft YaHei'] #用来显示中文，使用微软雅黑
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x = np.array([200, 600, 1000, 2000, 4000, 6000, 8000])
y_svm = np.array([0.962687, 0.956835, 0.963289, 0.962116, 0.965517, 0.967193, 0.965394])
y_bpnn = np.array([0.942687, 0.946835, 0.951001, 0.952001, 0.945517, 0.947193, 0.949394])

plt.plot(x, y_svm, label='SVM', marker='o')
plt.plot(x, y_bpnn, label='BPNN', marker='^')

plt.xlabel("消息数量")
plt.ylabel("TPR")

# plt.xticks(np.linspace(100, 1000, 10))
plt.yticks(np.linspace(0.8, 0.98, 6))

plt.legend()
plt.show()



