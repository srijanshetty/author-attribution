from __future__ import division
import nltk
import random
import re, pprint, os
import numpy
import glob
from nltk import cluster
from nltk.cluster import util
from nltk.cluster import api
from nltk.cluster import euclidean_distance
from nltk.cluster import cosine_distance
from nltk.cluster import KMeansClusterer
from nltk.collocations import *

# Empty list to hold all of the terms across documents, and another
# to hold text documents.
all_terms = []
texts = []
lentexts = []

# The directory to be parsed
path = "uni-corpus/*.split"
directories = glob.glob(path)
print "Tokenizing documents in the directories:", directories, "\n"

# Iterate through the directory and build the collection of texts and a list
# of terms for NLTK.
for directory in directories:
    print "-----------------------------------------------------------"
    print "Now tokenizing the directory:", directory
    print "-----------------------------------------------------------"
    files = glob.glob(directory + '/*')
    for infile in files:
        print "Now tokenizing the file:", infile
        if infile.startswith('.'): #Mac directories ALWAYS have a .DS_Store file.
            continue               #This ignores it and other hidden files.
        f = open(infile);
        raw = f.read()
        f.close()
        tokens = nltk.word_tokenize(raw)
        bitokens = nltk.bigrams(tokens)
        text = nltk.Text(bitokens)
        texts.append(text)
print "-----------------------------------------------------------"

# First we need to get the frequent collocations in the entire corpus
print "Computing the frequent bigrams of the corpus"
bigram_measures = nltk.collocations.BigramAssocMeasures()
corpus = open('corpus.txt').read()
finder = BigramCollocationFinder.from_words(corpus.split())
scoredBigram = finder.nbest(bigram_measures.raw_freq, 2000)
# scored = finder.score_ngrams(bigram_measures.raw_freq)
# scoredBigram = map(lambda (x,y): x, scored)

print "Using", len(scoredBigram), "frequent items"

# Function to create a BOW for one document.  For each of
# our unique words, we have a feature which is the count for that word
def BOWf(document):
    word_counts = []
    for bigram in scoredBigram:
        word_counts.append(document.count(bigram))
    return word_counts

### And here we actually call the function and create our list of vectors.
vectors = [numpy.array(BOWf(f)) for f in texts]
print "Vectors created."
print "First 10 words are", all_terms[:10]
print "First 10 counts for first document are", vectors[0][0:10]
#
# clusterer = KMeansClusterer(5, euclidean_distance)
# clusters = clusterer.cluster(vectors, assign_clusters=True, trace=False)
# means = clusterer.means()

