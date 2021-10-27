import csv

AUTHOR = 1
TITLE = 2
ID = 3
CONTENT = 4

with open('kaggle_poem_dataset.csv', newline='') as f:
    reader = csv.reader(f)
    for i in reader:
        print(i[AUTHOR])