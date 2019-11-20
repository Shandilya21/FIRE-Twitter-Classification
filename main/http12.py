import re
ft=open('File after twitter preprocessor','r',encoding='utf8')
###Twitter preprocessor(remove)-numbers,emoticons,smileys,mentions,reserved words
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)


for  i in ft:
	j=i
	j=re.sub(r'[(\'(\"\', )]',' ',j)
	j=re.sub(r'http\S+',' ', j,flags=re.I)
	j=re.sub(r'RT :','',j)
	j=re.sub(r' RT ',' ',j)
	j=re.sub(r':',' ',j)
	j=re.sub(r'! :',' ',j)
	#j=re.sub(r'u"\u2"\S',' ',j)
	j=emoji_pattern.sub(r'', j)
	print(j)
	#print(re.sub(r"/\S+",' ',i))
	#print(re.sub(r'@ \S+','',i))
	#if i!='\n':
		#print(i) 
