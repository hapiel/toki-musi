import csv
import sys

#to check what line of the csv file / what text is worked on
text_index = 0
construction_word = ''
current_word = ''


control_value = ''

def repeat_word_count(repeated_words, words):


    for element in words:
        if len(element) > 3:
            if words.count(element) > 1:
                raw_percentage = words.count(element) / len(words) * 100
                percentage = round(raw_percentage, 2)
                repeated_words.append([element, str(percentage) + "%"])

    # clean_repeated = list(dict.fromkeys(repeated_words))

    # used to check which line we are working on
    print("Text " + str(text_index))
    print(repeated_words)

    # reset repeated_words
    repeated_words = []

with open('../english/kaggle_poem_dataset.csv', newline='', encoding="utf-8") as csvfile:
    textreader = csv.reader(csvfile, delimiter=',')

    #for each poem
    for row in textreader:
        if row[0] == 'x':
            continue
        else:
            words = []
            repeated_words = []
            line = 0

            #updating the text index
            text_index += 1

            # to check the number of words in a poem
            word_count = 0

            #for each character in the poem create a python list of all words
            for i in row[4]:
                if i != ' ' and i != '\n' and i != ',' and i != ':' and i != '.' and i != '-' and i != '"' and i != '?' and i != '!' and i != '—' and i != '\xa0':
                    current_word = construction_word + i
                    construction_word = current_word
                #separation of words
                if i == ' ' or i == '\n':
                    word_count += 1
                    words.append(current_word)
                    construction_word = ''
                    if i == '\n':
                        line += 1
            #to have the correct amount of lines
            line += 1

            # print("Welcome to PoetGenerator 101.")
            # themeYesNo = input("Would you like to select a theme? (Enter 'Y' for YES or 'N' for NO) : ")
            # print("You entered : " + themeYesNo)
            # if (themeYesNo == "y" or themeYesNo == "Y"):
            #     theme = input("Please enter a word for the theme of your poem : ")
            #     print("You entered : " + theme)
            #
            # inputPoemYesNo = input("Would you like to enter a poem as a reference for the generated poem? (Enter 'Y' for YES or 'N' for NO) : ")
            # print("You entered : " + inputPoemYesNo)
            # if (inputPoemYesNo == "y" or inputPoemYesNo == "Y"):
            #     print("Please, copy/paste the poem you want to use as a reference : ")
            #     inputPoem = sys.stdin.readlines(6)
            #     print("You entered : " + str(inputPoem))


            #Call the repeated word function
            repeat_word_count(repeated_words, words)
            # print(line)


        #to have to correct amount of words
        word_count += 1

        # used to check the amount of words in a text
        #print(word_count)
        #print(words)



