# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Created on Sat Oct 14 10:16:56 2017

@author: Arunav
@author: Stitha
"""

import numpy as np
import operator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.neighbors import NearestCentroid
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.metrics.pairwise import cosine_similarity
from sklearn import metrics
from sklearn import svm
Y_id=np.empty(shape=[0,1])
Y=np.empty(shape=[0,1])
ft=open('Train.txt','r',encoding='utf8')
res=[]
for line in ft:
    if line=='\n':
        continue
    a=eval(line)
    Y_id=np.append(Y_id,a[1])
    Y=np.append(Y,a[0])
    res.extend(a[2].strip().split('\n'))
doc=list(res)
ft.close()

vec=TfidfVectorizer(sublinear_tf=True, max_df=0.1,norm='l1',stop_words='english')
X_t=vec.fit_transform(doc)
print(X_t.shape)
X=X_t[0:18231,0:]
Y=Y[0:18231]
print(X.shape)
avail=X_t[X_t.shape[0]-1,0:]
need=X_t[X_t.shape[0]-2,0:]
doc=np.asarray(doc)

sss = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=0)
sss.get_n_splits(X, Y)
for train_index, test_index in sss.split(X, Y):
    Y_id_test=Y_id[test_index]
    doc_test=doc[test_index]
    X_train, X_test = X[train_index], X[test_index] 
    Y_train, Y_test = Y[train_index], Y[test_index]
    
clf=NearestCentroid()
clf.fit(X_train, Y_train)
pred=clf.predict(X_test)
n=[]
a=[]
for i in range(pred.shape[0]):
    if pred[i]==2:
        n.append(i)
    elif pred[i]==3:
        a.append(i)
n=list(n)
a=list(a)

need_t=X_test[n]
need_doc=doc_test[n]
avail_t=X_test[a]


rank=cosine_similarity(need_t,need)

r=[]
r1=[]
for i in range(rank.shape[0]):
    r.append(rank[i,0])
rank=list(r)
sort1=zip(rank,need_doc)
sort1=sorted(sort1,key=operator.itemgetter(0))
for i in sort1:
    print(i)
rank1=cosine_similarity(avail_t,avail)
for i in range(rank1.shape[0]):
    r1.append(rank1[i,0])
rank1 = list(r1)


