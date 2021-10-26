import markovify
import os

combined_model = None
for (dirpath, _, filenames) in os.walk("text/tp_texts_small"):
    for filename in filenames:
        with open(os.path.join(dirpath, filename)) as f:
            # print (dirpath + " " + filename)
            model = markovify.Text(f, retain_original=False, state_size=3)
            if combined_model:
                combined_model = markovify.combine(models=[combined_model, model])
            else:
                combined_model = model


for i in range(5):
    print(combined_model.make_sentence())

