import spacy

def storyNER(storyFilePath):
    nlp = spacy.load("en_core_web_sm")
    with open(storyFilePath, encoding="utf-8") as storyFile:
        storyContent = storyFile.read()
        storyContentList = storyContent.split("\n")
        storyContentList = [line.strip() for line in storyContentList if line.strip()]
        storyContent = " ".join(storyContentList)

        analysisContent = nlp(storyContent)
        NERDictionary = {}
        for entities in analysisContent.ents:
            label = entities.label_
            text = entities.text
            if label not in NERDictionary:
                NERDictionary[label] = []
            NERDictionary[label].append(text)

        for label, entities in NERDictionary.items():
            print(f"{label}: {entities}")

if __name__ == "__main__":
    storyFile = "/Users/Jerry/Desktop/AsteXT/AsteXTCodeSummer2025/TheReasonWhy.txt"
    storyNER(storyFile)