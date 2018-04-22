from sklearn.neural_network import MLPClassifier

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


mpl = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)

print(mpl.fit(data_x, data_y))

x_test = data_x[10000:16000]
y_test = data_y[10000:16000]

acc, tpr, fpr = util.svm_result(mpl, x_test, y_test)

print('ACC: %f' % acc)
print('TPR: %f' % tpr)
print('FPR: %f' % fpr)


