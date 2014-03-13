from nltk import *
from pprint import pprint

file = open('temp')
text = file.read().decode('utf-8')
text = text.replace("\u0964", " ").replace("?", " ").replace("'", " ").replace("!", " ").replace(",", " ")
tokens = word_tokenize(text)
textBigrams = bigrams(tokens)
pprint(textBigrams)
