import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from dissertation import util
from sklearn import preprocessing

data = pd.read_csv('behaviour1.csv')

data_x = data[['PDR', 'PDFR', 'PMOR', 'PMR', 'Rs']]
data_y = data['Result']

data_x = preprocessing.scale(data_x)

x_train = data_x[0:10000]
y_train = data_y[0:10000]

svc = svm.SVC(kernel='linear', C=1).fit(x_train, y_train)
# svc = svm.SVC(kernel='rbf', gamma=0.4, C=20).fit(x_train, y_train)
# svc = svm.SVC(kernel='poly', degree=3, C=30, coef0=10).fit(x_train, y_train)
# svc = svm.SVC(kernel='sigmoid', coef0=-2.2, C=30).fit(x_train, y_train)

x_test = data_x[10000:15000]
y_test = data_y[10000:15000]

acc, tpr, fpr = util.svm_result(svc, x_test, y_test)

print(svc.kernel)
print('ACC: %f' % acc)
print('TPR: %f' % tpr)
print('FPR: %f' % fpr)


