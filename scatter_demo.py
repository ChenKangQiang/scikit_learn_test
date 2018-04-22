import matplotlib.pyplot as plt
import numpy as np

X = np.array([1, 2, 3, 4, 5, 6])
Y = np.array([1, 2, 3, 4, 5, 6])

# c=Y表示Y中的点依次的上色顺序为cmap
plt.scatter(X, Y, c=Y, cmap=plt.cm.Paired)
plt.show()

