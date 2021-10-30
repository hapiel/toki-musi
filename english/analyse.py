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
    wordSum = 0
    syllableSum = 0
    for line in lines:
        if(line == ""):
            noEmptyLines += 1
        wordSum += len(line.split())
        syllableSum += syllableCount(line)

    averageLineLength = wordSum / noLines
    averageSyllables = syllableSum / noLines

    return noLines, noEmptyLines, averageLineLength, averageSyllables

# with open('kaggle_poem_dataset.csv', newline='', encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for i in reader:
#         if(i[0] == 'x'):
#             continue
#         # Useful in case you want to check if it works quickly.
#         elif(i[0] == '20'):
#             break
#         noLines, noEmptyLines, averageLineLength, averageSyllables = analysePoem(i[CONTENT])

#         print(i[TITLE])
#         print("noLines: ", noLines)
#         print("noEmptylines: ", noEmptyLines)
#         print("averageLineLength: ", averageLineLength)
#         print("averageSyllables: ", averageSyllables)
#         print()

print(syllableCount("o toki mi wile ala moku e kili lili..."))