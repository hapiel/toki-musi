import markovify
import os
from pathlib import Path
import re

data_folder = Path("../tp_texts_small/")

combined_model = None
for (dirpath, _, filenames) in os.walk(data_folder):
    for filename in filenames:
        with open(os.path.join(dirpath, filename), encoding="utf-8") as f:
            # print (dirpath + " " + filename)
            model = markovify.Text(f, retain_original=False, state_size=3)
            if combined_model:
                combined_model = markovify.combine(models=[combined_model, model])
            else:
                combined_model = model

# store model as json
# model_json = combined_model.to_json()
# with open('data.json', 'w') as file:
#     file.write(model_json)

def string_end(string, wordcount):
    # return the last words of a string, without the special characters

    clean_string = re.sub(r"[^a-zA-Z0-9\s]","", string)
    
    if (len(clean_string.split())) >= wordcount:
        return " ".join(clean_string.split()[-wordcount:])
    else:
        return clean_string


sentence = combined_model.make_sentence(test_output = False, max_words=15)
print(sentence)

for i in range(5):
    # try to make a sentence with last 2 words of previous string
    try:
        sentence = combined_model.make_sentence_with_start(beginning=(string_end(sentence, 2)), strict=False, test_output = False, max_words=15)
    except:
        try:
            # try to make a sentence with last word of string
            sentence = combined_model.make_sentence_with_start(beginning=(string_end(sentence, 1)), strict=False, test_output = False, max_words=15)
        except:
            # make new sentence
            sentence = combined_model.make_sentence(test_output = False, max_words=15)
    
    print(sentence)

