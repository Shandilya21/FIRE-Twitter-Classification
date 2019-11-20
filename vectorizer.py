# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:53:57 2017

@author: Sthita
"""
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectKBest,chi2
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn import metrics
from sklearn.neighbors import NearestCentroid
from sklearn import svm
from nltk.stem import PorterStemmer as ps
from nltk.tokenize import sent_tokenize, word_tokenize
ft=open('Translated_final.txt','r',encoding='utf8')
results=[]
for line in ft:
    results.extend(line.strip().split('\n'))
doc=list(results)
ft.close()


fp=open('y_train.txt','r',encoding='utf8')
Y_id=np.empty(shape=[0,1])
Y_train=np.empty(shape=[0,1])
for i in fp.readlines():
    a=eval(i)
    Y_id=np.append(Y_id,a[0])
    Y_train=np.append(Y_train,a[1])
fp.close()



vec=TfidfVectorizer(sublinear_tf=True, max_df=0.1,norm='l1',stop_words='english')
X_train=vec.fit_transform(doc)
print(X_train.shape)
###print(X_train.todense())
feat_names=vec.get_feature_names()
#print(feat_names)
ch2 = SelectKBest(chi2, k=10000)
X_train = ch2.fit_transform(X_train,Y_train)
feat_names = [feat_names[i] for i
                         in ch2.get_support(indices=True)]

print(X_train.shape)


clf=MultinomialNB(alpha=.001)
clf.fit(X_train, Y_train)
pred=clf.predict(X_train)
print(metrics.precision_recall_fscore_support(Y_train,pred,average='weighted'))
print(metrics.f1_score(Y_train,pred,average='macro'))
