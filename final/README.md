# Toki pona poem generator
Created by: Daniel Siegmund, Semma Raadschelders & Anastasia Thambwe

Date: 8/11/2021

## Installation requirements:
- Python > 3.6
- [nltk](https://www.nltk.org/install.html), including the punkt submodule, this can be installed by running the following commands in your python interpreter after installing nltk:
```
>>> import nltk
>>> nltk download('punkt')
```
- [markovify library](https://github.com/jsvine/markovify), can be installed via pip:
```
$ pip install markovify
```
## How to run
- ```reverse.py``` generates a folder called reverse, which is the dataset, but with all the words reversed. If this folder is not present, or a different dataset is to be used, run this.
- ```poem_generator.py``` will generate the  markov models ```backwardsData.json``` and ```forwardsData.json``` if they are not present. It will then ask the user for input and generate a poem accordingly.
- ```modified_markovify.py``` and ```analyse.py``` supply functions to the poem generator. Running them does not generate output.
