import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn import model_selection

data = pd.read_csv('message1.csv')

data_x = data[['S_type', 'E_type', 'S_speed', 'S_acc', 'D1', 'D2', 'Rs', 'B', 'F_type', 'Rf']]
data_y = data['Result']

data_x = preprocessing.scale(data_x)

# svc = svm.SVC(kernel='linear', C=50)
svc = svm.SVC(kernel='rbf', gamma=0.1, C=40)
# svc = svm.SVC(kernel='poly', degree=3, C=20, coef0=10)
# svc = svm.SVC(kernel='sigmoid', coef0=-2, C=30)

scores1 = model_selection.cross_val_score(svc, data_x, data_y, cv=5)
scores2 = model_selection.cross_val_score(svc, data_x, data_y, cv=5, scoring='recall')

print('accuracy: {}, avg: {}'.format(scores1, np.mean(scores1)))
print('recall: {}, avg: {}'.format(scores2, np.mean(scores2)))



