
from random import randint, choice
import markovify
import os
from pathlib import PurePath
import analyse


from modified_markovify import  MarkovTextExtended, count_vowels

forwardsFolder = PurePath(os.path.dirname(__file__), "tp_texts_large")
backwardsFolder = PurePath(os.path.dirname(__file__), "reversed/tp_texts_large")

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


# phrase = "soweli suli"

# for i in range (11, 16):
#     backwards = backwardsModel.make_sentence_with_rules(syllables = randint(5,10), init_sentence=reverse(phrase))

#     forwards = forwardsModel.make_sentence_with_rules(syllables = i, init_sentence=reverse(backwards))
#     print(forwards)

input_poem, theme_phrase = analyse.userInterface()
line_count, empty_line_count, word_counts, syllable_counts = analyse.analysePoem(input_poem)


# print("\nSTATS")
# print("noLines: ", line_count)
# print("noEmptylines: ", empty_line_count)
# print("lineLenghts: ", word_counts)
# print("syllableCounts: ", syllable_counts)

poem_lines = []
print("\nTHE POEM: \n")
for i in range (0, line_count):
    if syllable_counts[i] == 0:
        poem_lines.append("")
        continue
    for tries in range(0, 1000):
        if i != 0:
            if randint(0,4) == 0:
                current_theme_phrase = theme_phrase
            elif randint(0,1) == 0:

                random_line = ""
                while random_line == "":
                    # pick a non empty line
                    random_line = choice(poem_lines)
                words = random_line.split()
                section_length = randint(1, len(words))
                start = randint(0, len(words)-section_length)
                current_theme_phrase = " ".join(words[start:start + section_length])
            else:
                random_line = ""
                while random_line == "":
                    # pick a non empty line
                    random_line = choice(poem_lines)
                current_theme_phrase = choice(random_line.split())
        else:
            current_theme_phrase = theme_phrase
        backwards = backwardsModel.make_sentence_with_rules(syllables = count_vowels(current_theme_phrase) + randint(0, max(0, syllable_counts[i] - count_vowels(current_theme_phrase))), init_sentence=reverse(current_theme_phrase))

        forwards = forwardsModel.make_sentence_with_rules(syllables = syllable_counts[i], init_sentence=reverse(backwards))

        if "ERROR" in forwards:
            continue
        poem_lines.append(forwards)
        break

for line in poem_lines:
    print(line)
    

