from random import randint
import markovify
import os
from pathlib import PurePath
import re

from modified_markovify import accumulate, MarkovChainExtended, MarkovTextExtended

forwardsFolder = PurePath(os.path.dirname(__file__), "../tp_texts_large")
backwardsFolder = PurePath(os.path.dirname(__file__), "../reversed/tp_texts_large")

def reverse(line):
    return " ".join(line.split()[::-1])

def buildModel(inputFolder, storeFile):
    model = None
    if os.path.isfile(PurePath(os.path.dirname(__file__), storeFile)):
        with open(PurePath(os.path.dirname(__file__), storeFile), 'r', encoding="utf-8") as file:
            model = MarkovTextExtended.from_json(file.read())
    else:
        for (dirpath, _, filenames) in os.walk(inputFolder):
            for filename in filenames:
                with open(os.path.join(dirpath, filename), encoding="utf-8") as f:
                    print (dirpath + " " + filename)
                    single_file_model = markovify.Text(f, retain_original=False, state_size=3)
                    if model:
                        model = markovify.combine(models=[model, single_file_model])
                    else:
                        model = single_file_model
        model_json = model.to_json()
        model = MarkovTextExtended.from_json(model_json)
        with open(PurePath(os.path.dirname(__file__), storeFile), 'w') as file:
            print("NEW DATABASE BUILT")
            file.write(model_json)

    return model

# delete json to rebuild the model

forwardsModel = buildModel(forwardsFolder, "forwardsData.json")
backwardsModel = buildModel(backwardsFolder, "backwardsData.json")


phrase = "soweli suli"

for i in range (11, 16):
    backwards = backwardsModel.make_sentence_with_rules(syllables = randint(5,10), init_sentence=reverse(phrase))

    forwards = forwardsModel.make_sentence_with_rules(syllables = i, init_sentence=reverse(backwards))
    print(forwards)
