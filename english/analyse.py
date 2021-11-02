import csv
from nltk.tokenize import SyllableTokenizer
from nltk import word_tokenize
import string

AUTHOR = 1
TITLE = 2
ID = 3
CONTENT = 4

def syllableCount(line):
    SSP = SyllableTokenizer()

    syllables = 0
    for token in word_tokenize(line):
        syllables += len(SSP.tokenize(token))

    return syllables

def analysePoem(poem):
    # Translation table used to remove punctuation and digits
    table_ = str.maketrans('', '', string.punctuation + string.digits + '”“’—')
    poem = poem.translate(table_)

    lines = poem.splitlines()
    noLines = len(lines)

    noEmptyLines = 0
    syllableCounts = []
    lineLenghts = []
    for line in lines:
        if(line == ""):
            noEmptyLines += 1
        lineLenghts.append(len(line.split()))
        syllableCounts.append(syllableCount(line))

    return noLines, noEmptyLines, lineLenghts, syllableCounts

with open('kaggle_poem_dataset.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    for i in reader:
        if(i[0] == 'x'):
            continue
        # Useful in case you want to check if it works quickly.
        elif(i[0] == '10'):
            break
        noLines, noEmptyLines, lineLenghts, syllableCounts = analysePoem(i[CONTENT])

        print(i[TITLE])
        print("noLines: ", noLines)
        print("noEmptylines: ", noEmptyLines)
        print("averageLineLength: ", lineLenghts)
        print("averageSyllables: ", syllableCounts)
        print()

