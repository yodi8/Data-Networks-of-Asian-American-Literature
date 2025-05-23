"""
Created on 5/23/25

@author: ryansi
"""

"""
Note from Ryan: 
The program isn't perfect, it makes a lot of mistakes when assigning *which*
languages are spoken (although it is pretty good with assigning *whether or not*
different languages are being spoken). This is particularly true because a lot 
of East-Asian languages share characters. Thus, each output spits out 
dictionary that determines which sentences were classified as multilingual. 
Double check the accuracy of that. 

The best way to fix that is to alter the minimum characters that a sentence 
must have to be considered. However, because a lot of Asian languages have less
characters/sentence, I need to keep it fairly low which decreases accuracy. 
If anybody has any way to fix this problem, feedback is appreciated. 
"""


from langdetect import detect, DetectorFactory, LangDetectException
from nltk.tokenize import sent_tokenize
import nltk

DetectorFactory.seed = 0


def analyze_languages(text, min_chars_per_sentence=2):
    """
    Scans `text` for language usage.

    Returns:
      multiple (bool)       – True if more than one language code is seen
      langs (set of str)    – all detected ISO-639-1 codes (e.g. {'en','es'})
      lang_sentences (dict) – maps each non-'en' code to a list of its sentences
    """
    sentences = sent_tokenize(text)
    langs = set()
    lang_sentences = {}

    for sent in sentences:
        # skip too-short bits that confuse the detector
        if len(sent) < min_chars_per_sentence:
            continue
        try:
            code = detect(sent)  # e.g. "en", "es", "fr"
            langs.add(code)
            # only keep non-English sentences in our dict
            if code != 'en':
                lang_sentences.setdefault(code, []).append(sent)
        except LangDetectException:
            # if it can’t classify, just ignore that sentence
            continue

    multiple = len(langs) > 1
    return multiple, langs, lang_sentences


text = """
Hello there. 
¿Dónde estás? 
Je suis ici. 
Just testing English again.
你好，我是司容灏.
司容灏喜欢喝奶茶。
"""

multiple, langs, lang_sentences = analyze_languages(text)
print("Multiple languages?", multiple)
print("All codes detected:", langs)
print("Non-English sentences:", lang_sentences)
