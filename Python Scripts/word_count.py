#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk
nltk.download('punkt')
nltk.download('stopwords') 
nltk.download('wordnet')
nltk.download('omw-1.4')

file = input('Please input the name of the text file: ')
try:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read() 
except Exception as e:
    print(e)
    print(f'File {file} not found.')
    file = input('Please try again with the full absolute path: ')
    try:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(e)
        print('The program exits.')
        exit()

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




