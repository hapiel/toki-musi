import csv



#to check what line of the csv file / what text is worked on
iter_count = 0

with open('../english/kaggle_poem_dataset.csv', newline='') as csvfile:
    textreader = csv.reader(csvfile, delimiter=',')
    for row in textreader:
        iter_count += 1
        # to check the number of words in a poem
        word_count = 0
        #print(row[4])

        for i in row[4]:
            if i == ' ' or i == '\n':
                word_count += 1

        #to have to correct amount of words
        word_count += 1
        print("Text " + str(iter_count))
        print(word_count)