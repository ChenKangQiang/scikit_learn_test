
import numpy as np
import pandas as pd
from sklearn.metrics import roc_curve, accuracy_score
from sklearn.model_selection import StratifiedKFold
from sklearn import svm
from sklearn import preprocessing

# #############################################################################
# Data IO and generation

data = pd.read_csv('../message1.csv')

data_x = data[['S_type', 'E_type', 'S_speed', 'S_acc', 'D1', 'D2', 'Rs', 'B', 'F_type', 'Rf']]
data_y = data['Result']

data_x = preprocessing.scale(data_x)

# #############################################################################
# Classification and ROC analysis

# Run classifier with cross-validation and plot ROC curves
cv = StratifiedKFold(n_splits=5)
# svc = svm.SVC(kernel='linear', C=50)
# svc = svm.SVC(kernel='rbf', gamma=0.1, C=40)
svc = svm.SVC(kernel='poly', degree=3, C=20, coef0=10)
# svc = svm.SVC(kernel='sigmoid', coef0=-2, C=30)

fprs = []
tprs = []
accuracies = []

for train, test in cv.split(data_x, data_y):
    result = svc.fit(data_x[train], data_y[train]).predict(data_x[test])
    fpr, tpr, thresholds = roc_curve(data_y[test], result)
    accuracy = accuracy_score(data_y[test], result)
    accuracies.append(accuracy)
    fprs.append(fpr[1])
    tprs.append(tpr[1])

print(svc)
print('fprs: {}, tprs: {}, accuracies: {}'.format(fprs, tprs, accuracies))
fpr_avg = np.mean(fprs)
tpr_avg = np.mean(tprs)
accuracy_avg = np.mean(accuracies)
print('fpr: {}, tpr: {}, accuracy: {}'.format(fpr_avg, tpr_avg, accuracy_avg))



