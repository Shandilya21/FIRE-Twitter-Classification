# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 10:16:56 2017

@author: sthita
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest,chi2
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.neighbors import NearestCentroid
from sklearn import metrics
from sklearn import svm
Y_id=np.empty(shape=[0,1])
Y=np.empty(shape=[0,1])
ft=open('Train.txt','r',encoding='utf8')
results=[]
for line in ft:
    if line=='\n':
        continue
    a=eval(line)
    Y_id=np.append(Y_id,a[1])
    Y=np.append(Y,a[0])
    
    results.extend(a[2].strip().split('\n'))
doc=list(results)

ft.close()

vec=TfidfVectorizer(sublinear_tf=True, max_df=0.1,norm='l1',stop_words='english')
X=vec.fit_transform(doc)
print(X.shape)
feat_names=vec.get_feature_names()
ch2 = SelectKBest(chi2, k=10000)
X = ch2.fit_transform(X,Y)
feat_names = [feat_names[i] for i
                         in ch2.get_support(indices=True)]

print(X.shape)
sss = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=0)
sss.get_n_splits(X, Y)
for train_index, test_index in sss.split(X, Y):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]
    
clf =svm.SVC(kernel='rbf')
clf.fit(X_train, Y_train)
pred=clf.predict(X_test)
print(metrics.confusion_matrix(Y_test,pred,labels=[1,2,3]))
print(metrics.precision_recall_fscore_support(Y_test,pred,average='weighted'))
#print(metrics.f1_score(Y_test,pred,average='macro'))

