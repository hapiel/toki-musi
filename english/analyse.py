import csv
from nltk.tokenize import SyllableTokenizer
from nltk import word_tokenize
import string
import random

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

def userInterface():
    inputPoem = ''

    #Beginning of the console printing
    print("Welcome to PoetGenerator 101.")

    #Questions about the theme and taking the user's input
    themeYesNo = input("Would you like to select a theme? (Enter 'Y' for YES or 'N' for NO) : ")

    if (themeYesNo == "y" or themeYesNo == "Y"):
        theme = input("Please enter a word for the theme of your poem : ")

    #Questions about the input poem and taking in the user's inputs
    inputPoemYesNo = input("Would you like to enter a poem as a reference for the generated poem? You will need to write the reference poem in the poem.txt file (Enter 'Y' for YES or 'N' for NO) : ")

    if (inputPoemYesNo == "y" or inputPoemYesNo == "Y"):

        poemNext = input("Please write or copy/paste your poem text in the poem.txt file present in this folder. Once you are done, enter 'Y': ")

        if (poemNext == 'y' or poemNext == 'Y'):
            with open('poem.txt') as f:
                inputPoem = f.read()
    else:
        with open('kaggle_poem_dataset.csv', newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            random_text_index = random.randint(1, 15651)
            for i in reader:
                if i[0] == 'x':
                    continue
                elif(int(i[0]) == random_text_index):
                    inputPoem = i[CONTENT]
                    break

    # print the string variable
    print("Poem used: ")
    print(inputPoem)

    return inputPoem

inputPoem = userInterface()

# with open('kaggle_poem_dataset.csv', newline='', encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for i in reader:
#         if(i[0] == 'x'):
#             continue
#         # Useful in case you want to check if it works quickly.
#         elif(i[0] == '10'):
#             break
#         print(i[CONTENT])
#         noLines, noEmptyLines, lineLenghts, syllableCounts = analysePoem(i[CONTENT])

#         print(i[TITLE])
#         print("noLines: ", noLines)
#         print("noEmptylines: ", noEmptyLines)
#         print("averageLineLength: ", lineLenghts)
#         print("averageSyllables: ", syllableCounts)
#         print()

