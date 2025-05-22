"""
Created on 5/22/25

@author: ryansi
"""
import spacy
import string

nlp = spacy.load('en_core_web_sm')

def LexicalDiversity(text):
  doc = nlp(text)

  totlength = len(text.split())

  lemmas = [token.lemma_.lower() for token in doc]
  lemmas1 = [lemma for lemma in lemmas if lemma not in string.punctuation and lemma not in nlp.Defaults.stop_words]

  lexdiv = len(set(lemmas1))

  if totlength == 0:
    return 0

  return lexdiv/(totlength)

if __name__ == '__main__':
    pass

text1 = "Hello hello hello hello. I greet you, and you greet me back. The repetition of the word 'hello' fills the air. It is said so often that it loses its meaning. I wonder, does repeating a word make it lose its importance? Or does it gain significance in its continuous usage? Hello, hello, hello, I say again, wondering if you hear it the same way each time."

text2 = "The cat sat on the mat, watching the world quietly. It sat there for a long time, looking outside the window, its paws tucked under its body. The mat seemed soft and comfortable, a perfect resting place for the cat. The afternoon sun filtered in, casting warm shadows on the floor. Despite the constant noise of the house, the cat remained calm, its eyes half-closed in peaceful repose. The world around it seemed distant, and the cat was lost in the quiet."

text3 = "Birds fly across the sky, their wings cutting through the air with ease. Fish swim in the clear blue waters, gliding smoothly beneath the surface. Dogs bark joyfully as they run in fields, chasing after sticks and balls. Cats, in contrast, purr quietly as they curl up in sunlit corners of the room. Each animal has its own rhythm, its own way of navigating the world. Together, they create a vibrant, living tapestry of life, with each creature contributing to the balance of nature."

text4 = "Every morning, the curious child set out to explore new places, meet strange people, and learn odd facts. The streets were filled with the sounds of the city—cars honking, people talking, and distant laughter. The child wandered through parks, observing the trees, the birds, and the way the sunlight filtered through the leaves. He discovered an old oak tree, its branches twisting like a maze, and climbed it to see the world from above. Each day was a new adventure, each moment filled with discovery and wonder."

text5 = "In the tangled forest of ideas and memories, moments shimmered with hidden meaning. The air was thick with stories and secrets, each step further revealing the layers of truth. Every path seemed to lead to another, each fork in the road opening up new possibilities. The forest was not made of trees, but of words, thoughts, and dreams, all intertwining to form a complex narrative. The deeper you ventured, the more intricate the connections became, and the more you wondered whether you were walking through the forest or if the forest was walking through you."


print(LexicalDiversity(text1))
print(LexicalDiversity(text2)) 
print(LexicalDiversity(text3))
print(LexicalDiversity(text4))
print(LexicalDiversity(text5))
