#!/usr/bin/env python
# coding: utf-8

# In[2]:


import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk
nltk.download('punkt')
nltk.download('stopwords') 
import os

file = input('Please input the full absolute path of the text file: ')

if not os.path.isfile(file):
    print("File does not exist. Please check your path.")
    exit()

with open(file, 'r', encoding='utf-8') as f:
    text = f.read()


words = word_tokenize(text)
words = [word.lower() for word in words if word.isalpha()]

stop_words = set(stopwords.words('english'))
stopwords = Counter(word for word in words if word in stop_words)
stopword_count = sum(stopwords.values())

print(f'Total words: {len(words)}')
for word, count in stopwords.most_common():
    print(f'{word}: {count}')
print(f'Stopwords count: {stopword_count}')
print(f'Percentage of stopwords: {round(stopword_count / len(words) * 100, 2)}%')



# In[ ]:




