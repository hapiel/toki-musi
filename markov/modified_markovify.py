import operator
import bisect
import markovify
import random

BEGIN = "___BEGIN__"
END = "___END__"

TRIES = 1000

rewarded_chars = ""

theme_word = ""

def count_vowels(string):
    num_vowels=0
    for char in string.lower():
        if char in "aeiou":
            num_vowels = num_vowels+1
    return num_vowels

def count_char(string, chars):
    num_chars=0
    for char in string.lower():
        if char in chars:
            num_chars = num_chars+1
    return num_chars

def accumulate(iterable, func=operator.add):
    """
    Cumulative calculations. (Summation, by default.)
    Via: https://docs.python.org/3/library/itertools.html#itertools.accumulate
    """
    it = iter(iterable)
    total = next(it)
    yield total
    for element in it:
        total = func(total, element)
        yield total


class MarkovChainExtended(markovify.Chain):
    def move(self, state):
        """
        Given a state, choose the next item at random.
        """
        if self.compiled:
            choices, cumdist = self.model[state]
        elif state == tuple([BEGIN] * self.state_size):
            choices = self.begin_choices
            cumdist = self.begin_cumdist
        else:
            choices, weights = zip(*self.model[state].items())
            new_weights = []
            for i, choice in enumerate(choices):
                if choice == theme_word:
                    new_weights.append(sum(weights)*2)
                else:
                    new_weights.append(weights[i])
                # else:
                #     new_weights.append(max(weights[i], weights[i] * (count_char(choice, rewarded_chars) * sum(weights))))
            cumdist = list(accumulate(new_weights))
        r = random.random() * cumdist[-1]
        selection = choices[bisect.bisect(cumdist, r)]
        
        return selection

class MarkovTextExtended(markovify.Text):
    

    def __init__(
        self,
        input_text,
        state_size=2,
        chain=None,
        parsed_sentences=None,
        retain_original=True,
        well_formed=True,
        reject_reg="",
    ):
        """
        input_text: A string.
        state_size: An integer, indicating the number of words in the model's state.
        chain: A trained markovify.Chain instance for this text, if pre-processed.
        parsed_sentences: A list of lists, where each outer list is a "run"
            of the process (e.g. a single sentence), and each inner list
            contains the steps (e.g. words) in the run. If you want to simulate
            an infinite process, you can come very close by passing just one, very
            long run.
        retain_original: Indicates whether to keep the original corpus.
        well_formed: Indicates whether sentences should be well-formed, preventing
            unmatched quotes, parenthesis by default, or a custom regular expression
            can be provided.
        reject_reg: If well_formed is True, this can be provided to override the
            standard rejection pattern.
        """

        
        self.well_formed = well_formed
        if well_formed and reject_reg != "":
            self.reject_pat = re.compile(reject_reg)

        can_make_sentences = parsed_sentences is not None or input_text is not None
        self.retain_original = retain_original and can_make_sentences
        self.state_size = state_size

        if self.retain_original:
            self.parsed_sentences = parsed_sentences or list(
                self.generate_corpus(input_text)
            )

            # Rejoined text lets us assess the novelty of generated sentences
            self.rejoined_text = self.sentence_join(
                map(self.word_join, self.parsed_sentences)
            )
            self.chain = chain or MarkovChainExtended(self.parsed_sentences, state_size)
            
        else:
            if not chain:
                parsed = parsed_sentences or self.generate_corpus(input_text)
            self.chain = chain or MarkovChainExtended(self.parsed_sentences, state_size)
    
    @classmethod
    def from_dict(cls, obj, **kwargs):
        return cls(
            None,
            state_size=obj["state_size"],
            chain=MarkovChainExtended.from_json(obj["chain"]),
            parsed_sentences=obj.get("parsed_sentences"),
        )

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

                if current_syllables == required_syllables:
                    if new_word == END:
                        break
                
                if current_syllables > required_syllables:
                    words = words[:-(random.randint(1, len(words)-3))]
                    continue

            if new_word == END:
                words = words[:-(random.randint(1, len(words)-3))]
                continue
            
            
            words = words + (new_word,)
            if i == TRIES -1:
                words =  words + ("ERROR",)
        
        # return words without the begin begin begin
        return " ".join(words[self.state_size:])