import csv

AUTHOR = 1
TITLE = 2
ID = 3
CONTENT = 4

def analysePoem(poem):
    lines = poem.splitlines()
    noLines = len(lines)
    
    noEmptyLines = 0
    sum = 0
    for line in lines:
        if(line == ""):
            noEmptyLines += 1
        words = line.split()
        sum += len(words)

    averageLineLength = sum / noLines

    return noLines, noEmptyLines, averageLineLength

with open('kaggle_poem_dataset.csv', newline='') as f:
    reader = csv.reader(f)
    for i in reader:
        # Useful in case you want to check if it works quickly.
        if(i[0] == '5'):
            break
        noLines, noEmptyLines, averageLineLength = analysePoem(i[CONTENT])

        print(i[TITLE])
        print("noLines: ", noLines)
        print("noEmptylines: ", noEmptyLines)
        print("averageLineLength: ", averageLineLength)
        print()