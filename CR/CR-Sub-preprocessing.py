from nltk.corpus import stopwords
s=stopwords.words('english')

temp=''

with open ('CR/test0.txt','r') as f:
    temp=f.read()

print (temp)