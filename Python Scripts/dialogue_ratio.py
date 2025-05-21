"""
Created on 2025/5/21
@author: Joyce Li
"""

import re

def calculate_dialogue_ratio(filepath):
    """
    Calculates the dialogue ratio of a text file.
    The dialogue ratio: percentage of words that appear inside quotation marks.
    """

    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()

    total = len(text.split())
    if total == 0:
        return 0.0

    dialogue_segments = re.findall(r'\"(.*?)\"', text, re.DOTALL)
    dialogue = sum(len(segment.split()) for segment in dialogue_segments)

    dialogue_ratio = dialogue / total
    return round(dialogue_ratio, 4)


if __name__ == '__main__':
    dialogue_ratio = calculate_dialogue_ratio("data/Kawano-OriginNemesis-1998.txt")
    print(f"Dialogue Ratio: {dialogue_ratio:.2%}")
