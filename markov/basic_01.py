import markovify

# Get raw text as string.
with open("text\soweli nasa - pipi pi moli luka.txt") as f:
    text = f.read()

# with open("text\english.txt") as f:
#     text = f.read()

# Build the model.
text_model = markovify.Text(text, state_size=2)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence(test_output=False))

# Print three randomly-generated sentences of no more than 280 characters
# for i in range(3):
#     print(text_model.make_short_sentence(280))