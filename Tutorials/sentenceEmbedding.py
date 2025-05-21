from sentence_transformers import SentenceTransformer, util
import nltk
from nltk.tokenize import sent_tokenize

model = SentenceTransformer("all-MiniLM-L6-v2")

def sentenceEmbedding(text):
    sentences = sent_tokenize(text)
    embeddings = model.encode(sentences)
    print("Finished embedding")
    return sentences, embeddings

def themeComparison(sentences, embeddings, themes):
    themeEmbeddings = model.encode(themes)
    threshold = 0.10
    for theme, themeEmbed in zip(themes, themeEmbeddings):
        scores = [util.cos_sim(sentenceEmbed, themeEmbed).item() for sentenceEmbed in embeddings]
        matchedSentences = [(sent, score) for sent, score in zip(sentences, scores) if score >= threshold]

        if matchedSentences:
            print(f"Theme: {theme}")
            for sentence, score in matchedSentences:
                print(f" - {sentence} (Score: {score:.2f})")
        else: 
            print(f"No matches found for theme: {theme}")

if __name__ == "__main__":
    themeList = ["literature", "children"]
    storyFile = "/Users/Jerry/Desktop/AsteXT/AsteXTCodeSummer2025/TheReasonWhy.txt"
    with open(storyFile) as file:
        storyContent = file.read()
        storyContentList = storyContent.split("\n")
        storyContentList = [line.strip() for line in storyContentList if line.strip()]
        storyContent = " ".join(storyContentList)

        sentences, embeddings = sentenceEmbedding(storyContent)
        themeComparison(sentences, embeddings, themeList)