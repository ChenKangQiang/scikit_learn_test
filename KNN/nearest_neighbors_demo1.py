from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
distances, indices = nbrs.kneighbors(X)

print(distances)
print(indices)

x_var = []
y_var = []

for s in X:
    x_var.append(s[0])
    y_var.append(s[1])

print(x_var)
print(y_var)

plt.scatter(x_var, y_var)
plt.show()
