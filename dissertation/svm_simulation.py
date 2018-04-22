import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from dissertation import util
from sklearn import preprocessing

data = pd.read_csv('message1.csv')

data_x = data[['S_type', 'E_type', 'S_speed', 'S_acc', 'D1', 'D2', 'Rs', 'B', 'F_type', 'Rf']]
data_y = data['Result']

data_x = preprocessing.scale(data_x)

x_train = data_x[0:10000]
y_train = data_y[0:10000]

# svc = svm.SVC(kernel='linear', C=50).fit(x_train, y_train)
svc = svm.SVC(kernel='rbf', gamma=0.1, C=40).fit(x_train, y_train)
# svc = svm.SVC(kernel='poly', degree=3, C=20, coef0=0.0).fit(x_train, y_train)
# svc = svm.SVC(kernel='sigmoid', coef0=-2, C=60).fit(x_train, y_train)

x_test = data_x[10000:18000]
y_test = data_y[10000:18000]

acc, tpr, fpr = util.svm_result(svc, x_test, y_test)

print(svc.kernel)
print('ACC: %f' % acc)
print('TPR: %f' % tpr)
print('FPR: %f' % fpr)


