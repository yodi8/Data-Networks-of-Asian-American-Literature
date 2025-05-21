from keybert import KeyBERT

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from gensim import corpora, models


keywordModel = KeyBERT(model='all-MiniLM-L6-v2')

#This function extracts keywords from one story
def extractKeyword(text):
    keywords = keywordModel.extract_keywords(text, candidates=None, keyphrase_ngram_range=(1, 1), stop_words='english', top_n=5, min_df=1, use_maxsum=False, use_mmr=False, diversity=0.9, nr_candidates=20, vectorizer=None, highlight=False, seed_keywords=None, doc_embeddings=None, word_embeddings=None, threshold=0.4)
    print(keywords)

#This function shows tipic modeling results
def topicModeling(text):
    stopWords = set(stopwords.words("english"))
    sentences = sent_tokenize(text)
    tokenizedWords = []
    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        words = [word for word in words if word.isalpha() and word not in stopWords]
        tokenizedWords.append(words)

    # wordCounter = {}
    # for sentence in tokenizedWords:
    #     for word in sentence:
    #         if word not in wordCounter:
    #             wordCounter[word] = 0
    #         wordCounter[word] += 1
    
    # wordList = wordCounter.items()
    # wordList = sorted(wordList, key=lambda x: x[1], reverse=True)
    # print(wordList[:10])
    
    dictionary = corpora.Dictionary(tokenizedWords)
    corpus = [dictionary.doc2bow(sentence) for sentence in tokenizedWords]

    lda = models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=3, passes=10, random_state=43)

    topics = lda.print_topics()
    for idx, topic in topics:
        print(f"Topic {idx}: {topic}")

if __name__ == "__main__":
    storyFile = "/Users/Jerry/Desktop/AsteXT/AsteXTCodeSummer2025/TheReasonWhy.txt"
    with open(storyFile) as file:
        storyContent = file.read()
        storyContentList = storyContent.split("\n")
        storyContentList = [line.strip() for line in storyContentList if line.strip()]
        storyContent = " ".join(storyContentList)
        # extractKeyword(storyContent)
        topicModeling(storyContent)