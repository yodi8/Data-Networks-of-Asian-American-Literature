# -*- coding: utf-8 -*-
import re
import syllapy
import string

file_name = "Li-TheReasonWhy-2020.txt"
path = "Short Stories As Text\\" + file_name

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

def words_per_sentece(text):
    count_words_per_sentence = []
    text = text.split(".")
    #print(text[1])
    for sentence in text:
        number_of_words = len(sentence.split())
        count_words_per_sentence.append(number_of_words)
    
    #print(count_words_per_sentence[1])

    result = sum(count_words_per_sentence)/len(count_words_per_sentence)
    return result
    

def flesch_reading_ease(text):
    score = (206.835 - 1.015*(words_per_sentence(text))
             - 84.6*(syllable_counter(text)/count_words(text)))
    return score

def syllable_counter(text):
    words = text.split()
    syllable_count = 0

    for word in words:
        word = word.strip(string.punctuation)
        syllable_count += syllapy.count(word)
    return syllable_count


with open(path, "r", encoding="utf-8") as file:
    text = file.read()
    print(f"Word Count: {count_words(text)}")
    print(f"Average word length: {average_word_length(text)}")
    print(f"Words Per Sentence: {words_per_sentece(text)}")
    print(f"Flesch Reading Score: {flesch_reading_ease(text)}")

