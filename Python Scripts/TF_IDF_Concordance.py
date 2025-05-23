#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.text import Text
from collections import Counter
import math
import string
import json

'''
This Python script provides a semi-automated method for identifying potential thematic keywords in a single short story using NLTK, without relying on an external corpus. The core idea is to approximate TF-IDF scoring by treating each sentence as an individual document. This is a pragmatic workaround during the early phase of our project, as we are still in the process of building a larger corpus of Asian American short stories.

The script performs the following steps:
1. Tokenizes and cleans the text by removing stopwords and punctuation.
2. Calculates a sentence-level pseudo-TF-IDF score for each word.
3. Selects the top-N keywords by score.
4. Retrieves full sentence-level context for each keyword (rather than using traditional concordance windows).
5. Outputs the results in a structured JSON file, allowing researchers to manually assess and label whether to retain each keyword.

This semi-automated approach is designed to support our human-in-the-loop workflow for dataset creation. It narrows the scope of candidate keywords so we can focus our interpretive labor more efficiently. Compared to raw word frequency, sentence-based TF-IDF gives more weight to words that are not just frequent but are unevenly distributed across the text—often indicative of thematic salience.

Additionally, working with this script has deepened my understanding of how to use NLTK in conjunction with other Python modules for natural language processing. It also helps us prepare for later tasks such as topic modeling, clustering, or semantic analysis.

However, this approach is not without limitations. I hope to address the following in future iterations and learning:

### Questions:

- If a word appears only a few times but always in emotionally intense sentences (e.g., “ashamed,” “belonging”), should it be considered more important than a high-frequency word with neutral contexts?
- Can TF-IDF capture emotional or rhetorical significance, or is it inherently blind to affect?
- Do co-occurring words like “mother” and “home” form latent “semantic alliances”? Can these be surfaced through concordance or co-occurrence graphs?
- How might the model be biased if most of the “documents” (i.e., sentences) are short or structurally repetitive?
- What does it mean to extract “keywords” from literary narratives, where ambiguity, irony, and voice are often central? Are we flattening the text in ways that undercut interpretation?
- Could hybrid approaches (TF-IDF + affective lexicon + part-of-speech constraints) offer a richer lens for keyword identification?
'''
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
# download necessary nltk data, if not downloaded

def load_and_clean_text(file_path):
    """
    This function would output a cleaned, tokenized word list and the original text 
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    tokens = word_tokenize(text.lower())  # Tokenize and lowercase
    stop_words = set(stopwords.words('english'))
    words = [word for word in tokens if word.isalnum() and word not in stop_words]
    return words, text
# Remove stopwords and punctuation and remain words and numbers

def extract_top_keywords_tfidf(words, text, top_n=10):
    """
    Calculate pseudo-TF-IDF for each word (treating each sentence as a document),
    and return the top 7 words with the highest TF-IDF scores

    """
    word_freq = Counter(words)
    total_words = len(words)
    sentences = sent_tokenize(text)  # split the original text into sentences
    tf_idf_scores = {}
    for word, freq in word_freq.items():
        tf = freq / total_words   # Term Frequency (TF) = word count / total words
        df = sum(1 for sentence in sentences if word in word_tokenize(sentence.lower()))   # Document Frequency (DF): number of sentences containing the word
        idf = math.log(len(sentences) / (df + 1)) # Inverse Document Frequency (IDF): log(total sentences / (df + 1))
        tf_idf_scores[word] = tf * idf
    return sorted(tf_idf_scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
    # sort the words by TF-IDF score descendingly and return the top 7 words

def find_sentences_with_keyword(text, keyword, max_sentences=3):
    """
    This function would return the sentences that contain the keyword
    """
    sentences = sent_tokenize(text)
    matched = [s.strip() for s in sentences if keyword in word_tokenize(s.lower())]
    return matched[:max_sentences] if matched else ["No context found"]

def create_keyword_report_json(file_path, top_n=7):
    words, text = load_and_clean_text(file_path)
    top_keywords = extract_top_keywords_tfidf(words, text, top_n)

    results = []
    for word, score in top_keywords:
        example_sentences = find_sentences_with_keyword(text, word)
        results.append({
            'Keyword': word,
            'TF-IDF Score': round(score, 4),
            'Example Sentences': example_sentences,
            'Keep': None
        })

    output_file = file_path.replace('.txt', '_tfidf_keyword_report.json')
    with open(output_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(results, jsonfile, indent=2, ensure_ascii=False)

    print(f"Keyword report saved to {output_file}")
    return output_file
    # output a json file

if __name__ == "__main__":
    file_path = input("Enter the path to your text file: ")
    create_keyword_report_json(file_path, top_n=10)


# In[ ]:




