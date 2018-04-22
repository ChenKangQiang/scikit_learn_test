import numpy as np
import matplotlib.pyplot as plt

data = [1, 2, 3, 4, 5, 6]
# 打印前面两个数字
print(data[:2])

X, Y = np.meshgrid([1, 2, 3], [4, 5, 6, 7])


xx = X.ravel()

print(X)
print(Y)

# 矩阵进行连接
Z = np.c_[X, Y]
print(Z)
print(np.c_[X.ravel(), Y.ravel()])

# 将多维矩阵分开，转成一维矩阵
xx = X.ravel()
print(xx)
print("the shape of xx is %d" % xx.shape)

# 打印数组的shape
print(np.array([[1, 2, 3], [4, 5, 6]]).shape)
print(np.array([1, 2, 3, 4, 5, 6]).shape)

print(plt.xticks())

# 画图操作
# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# plt.plot(x, y)
# plt.show()

print(np.random.randn(20, 2))
print([0] * 20 + [1] * 20)

print(2 * [1, 2, 3, 4])

print(np.random.random((100, 200)))
print((2 * np.random.random((100, 200))).shape)

# 数组乘以某个数
print(2 * np.array([1, 3, 4, 6]))  # [2, 6, 8, 12]
# 列表乘以某个数
print(2 * [1, 3, 4, 6])  # [1, 3, 4, 6, 1, 3, 4, 6]



