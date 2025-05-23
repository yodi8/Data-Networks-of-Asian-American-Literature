"""
Created on 5/23/25

@author: ryansi
"""

import ssl

# ─── allow downloads without SSL certificate checks ───
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # older Python that doesn’t support it: nothing to do
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context



import nltk
from nltk.corpus import opinion_lexicon
from nltk.tokenize import word_tokenize

# now these will work:
nltk.download('punkt')
nltk.download('opinion_lexicon')
nltk.download('punkt_tab')

positive_words = set(opinion_lexicon.positive())
negative_words = set(opinion_lexicon.negative())


def emotion_stats(text):
    """
    Analyzes a text and returns:
      total_words       – the total token count
      emo_count         – how many tokens are emotional (pos or neg)
      density           – emo_count / total_words
      positive_count    – how many tokens are in the positive list
      negative_count    – how many tokens are in the negative list
      positive_ratio    – positive_count / emo_count (or 0 if no emotional words)
      negative_ratio    – negative_count / emo_count (or 0 if no emotional words)
    """
    # 1. Tokenize into lowercase words
    tokens = word_tokenize(text.lower())
    total_words = len(tokens)

    # 2. Count positives and negatives separately
    positive_count = sum(tok in positive_words for tok in tokens)
    negative_count = sum(tok in negative_words for tok in tokens)

    # 3. Emotional total and overall density
    emo_count = positive_count + negative_count
    density = emo_count / total_words if total_words else 0

    # 4. Within-emotion proportions
    if emo_count:
        positive_ratio = positive_count / emo_count
    else:
        positive_ratio = negative_ratio = 0

    # 5. Package results
    return {
        'emo_count'      : emo_count,
        'density'        : density,
        'positive_count' : positive_count,
        'negative_count' : negative_count,
        'positive_ratio' : positive_ratio,
    }


sample = "I love sunny days, though sometimes the heat makes me angry or sad."
stats  = emotion_stats(sample)
print(stats)
