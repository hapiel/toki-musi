import markovify
import os
from pathlib import Path

data_folder = Path("text/tp_texts_small/")

combined_model = None
for (dirpath, _, filenames) in os.walk(data_folder):
    for filename in filenames:
        with open(os.path.join(dirpath, filename)) as f:
            # print (dirpath + " " + filename)
            model = markovify.Text(f, retain_original=False, state_size=3)
            if combined_model:
                combined_model = markovify.combine(models=[combined_model, model])
            else:
                combined_model = model


for i in range(5):
    print(combined_model.make_sentence_with_start(beginning=("jan pona"), strict=False, test_output = False, max_words=15))

