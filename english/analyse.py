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

def words_list_maker(text):
    words = []
    current_word = ''
    construction_word = ''
    for i in text:
        if i != ' ' and i != '\n' and i != ',' and i != ':' and i != '.' and i != '-' and i != '"' and i != '?' and i != '!' and i != '—' and i != '\xa0':
            current_word = construction_word + i
            construction_word = current_word
            # separation of words
        else:
            if current_word != '':
                words.append(current_word)
                current_word = ''
                construction_word = ''

    for word in words:
        if len(word) == 0:
            words.remove(word)

    return words

def repeat_word_count(words):
    repeated_words = []
    for element in words:
        if len(element) > 3:
            if words.count(element) > 1:
                raw_percentage = words.count(element) / len(words) * 100
                percentage = round(raw_percentage, 2)
                repeated_words.append([element, str(percentage) + "%"])

    return repeated_words

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
    inputPoem = None

    #Beginning of the console printing
    print("Welcome to PoetGenerator 101.")

    themeSpecified = False
    while(not themeSpecified):
        #Questions about the theme and taking the user's input
        themeYesNo = input("Would you like to select a theme? (Enter 'Y' for YES or 'N' for NO) : ")

        if (themeYesNo == "y" or themeYesNo == "Y"):
            theme = input("Please enter a word for the theme of your poem : ")
            themeSpecified = True
        elif(themeYesNo.lower() == 'n'):
            theme = None
            themeSpecified = True

    while(inputPoem == None):
        #Questions about the input poem and taking in the user's inputs
        inputPoemYesNo = input("Would you like to enter a poem as a reference for the generated poem? You will need to write the reference poem in the poem.txt file (Enter 'Y' for YES or 'N' for NO) : ")

        if (inputPoemYesNo == "y" or inputPoemYesNo == "Y"):
            poemNext = input("Please write or copy/paste your poem text in the poem.txt file present in this folder. Once you are done, enter 'Y': ")
            if (poemNext == 'y' or poemNext == 'Y'):
                with open('poem.txt') as f:
                    inputPoem = f.read()
        elif(inputPoemYesNo.lower() == 'n'):
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

    return inputPoem, theme

inputPoem, theme = userInterface()
noLines, noEmptyLines, lineLenghts, syllableCounts = analysePoem(inputPoem)

# words = words_list_maker(inputPoem)
# repeatedWords = repeat_word_count(words)

print("\nSTATS")
print("noLines: ", noLines)
print("noEmptylines: ", noEmptyLines)
print("lineLenghts: ", lineLenghts)
print("syllableCounts: ", syllableCounts)
# print("words: ", words)
# print("repeatedWords: ", repeatedWords)
print()