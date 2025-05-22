#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string

def clean_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation)) 
    return text.lower()  # delete all punctuation and convert all words to lowercase

def calculate_lexical_diversity(text):
    words = clean_text(text).split()
    return len(set(words)) / len(words)  # use split to create list and set() to delete repetitive words

filename = input('Please input the name of your file: ')
try:
    with open(filename, 'r') as f:
        text = f.read()
    score = calculate_lexical_diversity(text)
    words = clean_text(text).split()
    print(f'\nLexical Diversity Score: {score}')
    print(f'Total Words: {len(words)}')
    print(f'Unique Words: {len(set(words))}')

except Exception as e:
    print(e)
    file = input('Please try again with the full absolute path: ')
    try:
        with open(file, 'r') as f:
            text = f.read()
    except Exception as e:
        print(e)
        print('The program exits.')
        exit()

