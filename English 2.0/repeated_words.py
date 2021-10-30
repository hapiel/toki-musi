import csv



#to check what line of the csv file / what text is worked on
line_number = 0
construction_word = ''
current_word = ''


control_value = ''

with open('../english/kaggle_poem_dataset.csv', newline='') as csvfile:
    textreader = csv.reader(csvfile, delimiter=',')

    #for each poem
    for row in textreader:
        if row[0] == 'x':
            continue
        else:
            words = []
            repeated_words = []
            #updating the line number
            line_number += 1

            # to check the number of words in a poem
            word_count = 0

            #for each character in the poem
            for i in row[4]:
                if i != ' ' and i != '\n' and i != ',' and i != ':' and i != '.' and i != '-' and i != '"' and i != '?' and i != '!' and i != '—' and i != '\xa0':
                    current_word = construction_word + i
                    construction_word = current_word
                if i == ' ' or i == '\n':
                    word_count += 1
                    words.append(current_word)
                    construction_word = ''

            # checking all repeating words
            for element in words:
                if len(element) > 3:
                    if words.count(element) > 1:
                        repeated_words.append(element)


            # used to check which line we are working on
            print("Text " + str(line_number))
            #print('\n')
            print(repeated_words)


            #reset repeated_words
            repeated_words = []

            # for i in words:
            #     control_value = i
            #     continue
            #
            #     if (i == control_value) and (i != 'a') and (i != 'I') and (i != 'the') and (i != 'is'):
            #         repeated_words.append(i)
            #         control_value = ''

        #to have to correct amount of words
        word_count += 1

        # used to check the amount of words in a text
        #print(word_count)
        #print(words)





