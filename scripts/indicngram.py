from indicngramlib import *
from sys import argv

filename, input_file, output_file = argv

ngram = indicNgram()
ngram.bigram(input_file)
ngram.printBifreq(output_file)
# It will print the output to command line
