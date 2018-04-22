import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams['font.sans-serif']=['SimHei']

plt.rcParams['font.sans-serif']=['Microsoft YaHei'] #用来显示中文，使用微软雅黑
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# x = np.linspace(200, 8200, 20)
x = np.array([200, 600, 1000, 2000, 4000, 7000, 10000])
y_svm = np.array([0.858209, 0.898551, 0.913363, 0.938528, 0.950790, 0.956747, 0.966551])
y_bpnn = np.array([0.808209, 0.844389, 0.871453, 0.908658, 0.930765, 0.945765, 0.959000])

plt.plot(x, y_svm, label='SVM', marker='o')
plt.plot(x, y_bpnn, label='BPNN', marker='^')

plt.xlabel("训练样本数量")
plt.ylabel("TPR")

# plt.xticks(np.linspace(100, 1000, 10))
plt.yticks(np.linspace(0.8, 0.98, 6))

plt.legend()
plt.show()



