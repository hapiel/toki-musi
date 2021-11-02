import markovify
import os
from pathlib import PurePath
import re


from modified_markovify import accumulate, MarkovChainExtended, MarkovTextExtended


data_folder = PurePath(os.path.dirname(__file__), "../tp_texts_large")


# delete data.json to rebuild the model

model = None

if os.path.isfile("data.json"):
    with open('data.json', 'r', encoding="utf-8") as file:
        model = MarkovTextExtended.from_json(file.read())
else:
    for (dirpath, _, filenames) in os.walk(data_folder):
        for filename in filenames:
            with open(os.path.join(dirpath, filename), encoding="utf-8") as f:
                # print (dirpath + " " + filename)
                single_file_model = markovify.Text(f, retain_original=False, state_size=3)
                if model:
                    model = markovify.combine(models=[model, single_file_model])
                else:
                    model = single_file_model
    model_json = model.to_json()
    model = MarkovTextExtended.from_json(model_json)
    with open('data.json', 'w') as file:
        file.write(model_json)


def string_end(string, wordcount):
    # return the last words of a string, without the special characters

    clean_string = re.sub(r"[^a-zA-Z0-9\s]","", string)
    
    if (len(clean_string.split())) >= wordcount:
        return " ".join(clean_string.split()[-wordcount:])
    else:
        return clean_string


for i in range(1, 10):
    print(model.make_sentence_with_rules(syllables=i))


# print(model.make_sentence_with_rules(syllables=1))
print(model.make_sentence_with_rules(syllables=10))
print(model.make_sentence_with_rules(syllables=10))
print(model.make_sentence_with_rules(syllables=10))
