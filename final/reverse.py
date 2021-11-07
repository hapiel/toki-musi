from pathlib import Path
from nltk import word_tokenize

import os

data_folder = Path("tp_texts_large/")

for (dirpath, _, filenames) in os.walk(data_folder):
    for filename in filenames:
        oldPath = os.path.join(dirpath, filename)
        newFolder = os.path.join('reversed/', dirpath)
        Path(newFolder).mkdir(parents=True, exist_ok=True)
        newPath = os.path.join(newFolder, filename)
        newFile = open(newPath, "w")
        with open(oldPath, encoding="utf-8") as oldFile:
            linesReversed = oldFile.readlines()[::-1]
            for line in linesReversed:
                tokens = word_tokenize(line)
                line = [token if not (token == '.' or token == '?' or token == '!') else '\n' for token in tokens][::-1]
                newFile.write(" ".join(line) + "\n")
        newFile.close()
        