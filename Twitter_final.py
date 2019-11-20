Developer_="Arunav Pratap Shandeelya"
_College_="IIIT Bhubaneswar"
_Mentor_="Dr. Rakesh Chandra Balbantray"
_Project_="Forum for Information Retreival Govt of India"
_Version_="1.0"
_Status_="Development"



import re
import json
import numpy as np
import preprocessor as p
import pickle as pk
from googletrans import translator
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import SelectKBest,chi2
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn import metrics


#Extracting from JSONL file
f=open("NepalQuake-code-mixed-training-tweets.jsonl",'r',encoding='utf8');
g= open("Extracted.txt", 'a',encoding='utf8');
for i in f:
	j=json.loads(i);
	j=j['text'];
	h=json.dumps(j);
	#JSONDecoder for Decoding from .Jsonl File..
	a=json.JSONDecoder().raw_decode(h) 
	g.write(str(a))
	g.write('\n')
f.close()
g.close()
	##print (a)



#Opening of Extracted text after Decoding 
f1 = open("Extracted.txt",'r',encoding='utf8');
g1 = open("Preprocessed.txt",'a',encoding='utf8');
#Tweet Preprocessing through Preprocessor:URL,Emoji,Numbers etc.
p.set_options(p.OPT.URL, p.OPT.EMOJI,p.OPT.MENTION,p.OPT.RESERVED,p.OPT.SMILEY,p.OPT.NUMBER)
for s in f1:
	v = (p.clean(s))
	g1.write(v)
	g1.write('\n')
	##print (v) 
f1.close()
g1.close()
		

f2 = open("Preprocessed.txt",'r',encoding = 'utf8')
g2 = open("Tweetcleaned.txt",'1',encoding = 'utf8')
#cleaning the tweets by re module for unwanted  emoticon,reserved,number

emojis_pattern = re.compile("["
	u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    u"\U0001F1E0-\U0001F1FF"  # flags (ioS)
                            "]+",flags=re.UNICODE)

for p in f2:
	j=p
	j=j.replace(r'\n',' ')
	a=eval(j)
	j=a[0]
	j=re.sub(r'[(\'(\"\', )]',' ',j)
	j=re.sub(r'http\S+',' ', j,flags=re.I)
	j=re.sub(r'RT :','',j)
	j=re.sub(r' RT ',' ',j)
	j=re.sub(r':',' ',j)
	j=re.sub(r'! :',' ',j)
	##j=re.sub(r'u"\u2"\S',' ',j)
	j=re.sub(r'\n',' ',j)
	j=emojis_pattern.sub(r'', j)
	g2.write(j)
f2.close()
g2.close()

## Translation through GoogleTranslate API

ft=open('Tweetcleaned.txt','r',encoding='utf8')
ft1=open('Translated_final.txt','a',encoding='utf8')
trans=Translator()
for i in ft:
	if i=='\n':
		continue
	g.write(trans.translate(i,dest='en').text)
	g.write('\n')
ft.close()
ft1.close()
##Stripping the Translated data

f3=open('Translated_final.txt','r',encoding='utf8')
results=[]
for line in fq:
    results.extend(line.strip().split('\n'))
doc=list(results)
fq.close()


fr=open('y_train.txt','r',encoding='utf8')

Y_id=np.empty(shape=[0,1])
Y_train=np.empty(shape=[0,1])
for i in fr.readlines():
    a=eval(i)
    Y_id=np.append(Y_id,a[0])
    Y_train=np.append(Y_train,a[1])
fr.close()


##calculating Tf-idf score of the Tweets and training the data

vec=TfidfVectorizer(sublinear_tf=True, max_df=0.1,norm='l1',stop_words='english')
X_train=vec.fit_transform(doc)
print(X_train.shape)
###print(X_train.todense())
feat_names=vec.get_feature_names()
#print(feat_names)

##chi2 module for 'Feature Selection' of target data

ch2 = SelectKBest(chi2, k=10000)
X_train = ch2.fit_transform(X_train,Y_train)
feat_names = [feat_names[i] for i
                         in ch2.get_support(indices=True)]

print(X_train.shape)

## Multinomial Naive_Bayes Algorithm

clf=MultinomialNB(alpha=.001)
clf.fit(X_train, Y_train)
pred=clf.predict(X_train)

print(metrics.precision_recall_fscore_support(Y_train,pred,average='weighted'))
print(metrics.f1_score(Y_train,pred,average='macro'))






	

		  

         
        





	
		


		






	