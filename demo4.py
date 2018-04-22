import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams['font.sans-serif']=['SimHei']

plt.rcParams['font.sans-serif']=['SimHei'] #用来显示中文，使用黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x = np.linspace(100, 500, 10)
y1 = np.array(np.random.rand(10, 1))
y2 = np.array([0.8, 0.9, 0.45, 0.56, 0.78, 0.42, 0.93, 0.67, 0.46, 0.89])

plt.plot(x, y1, label='SVM', marker='o')
plt.plot(x, y2, label='BPNN', marker='^')

plt.title("测试")

plt.xlabel("numbers")
plt.ylabel("TPR")

plt.legend()

plt.show()

