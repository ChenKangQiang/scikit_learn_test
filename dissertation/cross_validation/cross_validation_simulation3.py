import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_curve
from sklearn.metrics import accuracy_score

data = pd.read_csv('../behaviour1.csv')

data_x = data[['PDR', 'PDFR', 'PMOR', 'PMR', 'Rs']]
data_y = data['Result']

data_x = preprocessing.scale(data_x)

cv = StratifiedKFold(n_splits=5)

# svc = svm.SVC(kernel='linear', C=20)
# svc = svm.SVC(kernel='rbf', gamma=0.4, C=30)
# svc = svm.SVC(kernel='poly', degree=4, C=20, coef0=5)
svc = svm.SVC(kernel='sigmoid', coef0=-2.2, C=50)

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


