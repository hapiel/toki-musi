import markovify
import os
from pathlib import Path
import re
from random import randint
import json

#needed to extend markovify.chain
BEGIN = "___BEGIN__"
END = "___END__"

TRIES = 1000

data_folder = Path("../tp_texts_small/")

def count_vowels(string):
    num_vowels=0
    for char in string.lower():
        if char in "aeiou":
            num_vowels = num_vowels+1
    return num_vowels

class MarkovChainExtended(markovify.Chain):
    pass

class MarkovTextExtended(markovify.Text):
    def make_sentence_with_rules(self, init_state=None, **kwargs):
        
        required_syllables = kwargs.get("syllables", None)

        if init_state is None:
            prefix = []
        else:
            prefix = list(init_state)
            for word in prefix:
                if word == BEGIN:
                    prefix = prefix[1:]
                else:
                    break
        
        # set the words tuple to BEGIN BEGIN BEGIN, as many begins as state_size
        words = ()
        for _ in range (0, self.state_size):
            words = words + (BEGIN,)


        # make sentence
        for i in range (0, TRIES):
            new_word = self.chain.move(words[-self.state_size:])

            if required_syllables != None:

                current_syllables = count_vowels(" ".join(words[self.state_size:]))
                # print("Syllables:" + str(current_syllables))

                if current_syllables == required_syllables:
                    # print(words)
                    if new_word == END:
                        # print(words)
                        break
                
                if current_syllables > required_syllables:
                    # words = words[:-(randint(1, len(words)-3))]
                    words = words[:-(randint(1, len(words)-3))]
                    # print(("test", ) + words)
                    continue

            if new_word == END:
                words = words[:-(randint(1, len(words)-3))]
                continue
            
            
            words = words + (new_word,)
            if i == TRIES -1:
                words =  words + ("ERROR",)
        
        # return words without the begin begin begin
        return " ".join(words[self.state_size:])


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
                single_file_model = MarkovTextExtended(f, retain_original=False, state_size=3)
                if model:
                    model = markovify.combine(models=[model, single_file_model])
                else:
                    model = single_file_model
    model_json = model.to_json()
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




