# -*- coding: utf-8 -*-
import re

file_name = "1.txt"
path = "Short Stories As Text"

def remove_all_symbols(text):
    return re.sub(r'[^A-Za-z\s]', '', text)

def count_words(text):
    return len(text.split())

def average_word_length(text):
    words = text.split()
    words_without_symbols = []
    if len(words) == 0:
        return 0
    
    for word in words:
        word = remove_all_symbols(word)
        words_without_symbols.append(word)

    word_length = [len(word) for word in words_without_symbols]
    average = sum(word_length)/len(word_length)
    
    return average



with open(file_name, "r", encoding="utf-8") as file:
    text = file.read()
    print(f"Word Count: {count_words(text)}")
    print(f"Average word length: {average_word_length(text)}")

