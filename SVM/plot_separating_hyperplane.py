"""
=========================================
SVM: Maximum margin separating hyperplane
=========================================

Plot the maximum margin separating hyperplane within a two-class
separable dataset using a Support Vector Machine classifier with
linear kernel.
"""
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# we create 40 separable points
np.random.seed(0)
X = np.r_[np.random.randn(20, 2) - [3, 3], np.random.randn(20, 2) + [3, 3]]
Y = [0] * 20 + [1] * 20

# fit the model
clf = svm.SVC(kernel='linear')
clf.fit(X, Y)

# get the separating hyperplane
w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(-5, 5)
yy = a * xx - (clf.intercept_[0]) / w[1]

yy1 = (a+1) * xx - (clf.intercept_[0]) / w[1] + 1
yy2 = (a-1) * xx - (clf.intercept_[0]) / w[1] + 1
yy3 = a * xx - (clf.intercept_[0]) / w[1] - 2
yy4 = a * xx - (clf.intercept_[0]) / w[1] + 2


# plot the parallels to the separating hyperplane that pass through the
# support vectors
b = clf.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = clf.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])

# plt.subplot(121)

# plot the line, the points, and the nearest vectors to the plane
plt.plot(xx, yy, 'k-', color="k", linewidth=2)
# plt.plot(xx, yy_down, 'k--')
# plt.plot(xx, yy_up, 'k--')

plt.plot(xx, yy1, 'k-', color='b', linewidth=1)
plt.plot(xx, yy2, 'k-', color='y', linewidth=1)
plt.plot(xx, yy3, 'k-', color='c', linewidth=1)
plt.plot(xx, yy4, 'k-', color='r', linewidth=1)

plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
            s=80, facecolors='none')
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)

plt.axis('tight')
plt.xticks(())
plt.yticks(())


# plt.subplot(122)
# plt.plot(xx, yy, 'k-', color="r", linewidth=3)
# plt.plot(xx, yy_down, 'k--')
# plt.plot(xx, yy_up, 'k--')
#
# plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
#             s=80, facecolors='none')
# plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)
#
# plt.axis('tight')
# plt.xticks(())
# plt.yticks(())

plt.show()
