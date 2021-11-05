import csv
import sys
import random

#to check what line of the csv file / what text is worked on
text_index = 0 #a text index value used when the code goes over every single poem of the database, one by one (the value is increment with each peom that is covered
construction_word = ''
current_word = ''
random_text_index = random.randint(1, 15651)
inputPoem = ''
word_count = 0
words = []



control_value = ''

def words_list_maker(text):
    words = []
    current_word = ''
    construction_word = ''
    for word in text:
        if word != ' ' and word != '\n' and word != ',' and word != ':' and word != '.' and word != '-' and word != '"' and word != '?' and word != '!' and word != '—' and word != '\xa0':
            current_word = construction_word + word
            construction_word = current_word
            # separation of words
        if word == ' ' or word == '\n':
            words.append(current_word)
            construction_word = ''
    return words

def repeat_word_count(repeated_words, words):


    for element in words:
        if len(element) > 3:
            if words.count(element) > 1:
                raw_percentage = words.count(element) / len(words) * 100
                percentage = round(raw_percentage, 2)
                repeated_words.append([element, str(percentage) + "%"])

    # clean_repeated = list(dict.fromkeys(repeated_words))

    # used to check which line we are working on
    print("Text " + str(random_text_index))
    print(repeated_words)

    # reset repeated_words
    repeated_words = []

print("Welcome to PoetGenerator 101.")
# themeYesNo = input("Would you like to select a theme? (Enter 'Y' for YES or 'N' for NO) : ")
# print("You entered : " + themeYesNo)
# if (themeYesNo == "y" or themeYesNo == "Y"):
#     theme = input("Please enter a word for the theme of your poem : ")
#     print("You entered : " + theme)


inputPoemYesNo = input(
    "Would you like to enter a poem as a reference for the generated poem? You will need to specify how many characters this poem has (Enter 'Y' for YES or 'N' for NO) : ")
print("You entered : " + inputPoemYesNo)


if (inputPoemYesNo == "y" or inputPoemYesNo == "Y"):
    characters_input_poem = input("Please enter the amount of characters your poem has : ")
    print("Please, copy/paste the poem you want to use as a reference and press the key 'ENTER' : ")
    inputPoemLines = sys.stdin.readlines(int(characters_input_poem))

    # this loop is used to transfer the text that was entered into a string variable
    for line in inputPoemLines:
        inputPoem += line

    # print the string variable
    print("You entered : ")
    print(inputPoem)

    #English analysis functions for the input poem
    words = words_list_maker(inputPoem)
    print(words)
    
    #repeat_word_count()

else:
    # English analysis functions for the database random poem

    with open('../english/kaggle_poem_dataset.csv', newline='', encoding="utf-8") as csvfile:
        textreader = csv.reader(csvfile, delimiter=',')

        #for each poem
        for row in textreader:
            if row[0] == 'x':
                continue
            elif int(row[0]) == random_text_index:
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

                # Call the repeated word function
                repeat_word_count(repeated_words, words)





            #to have to correct amount of words
            #word_count += 1

            #used to check the amount of words in a text
            # print(word_count)
            # print(words)



