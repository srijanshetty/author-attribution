# coding: utf-8
import glob

# If key exists return it
def get_key(line):
    temp = line.strip().split(' ')
    try:
        if temp[1]:
            return temp[1]
    except IndexError:
        pass

# If key exists return true
def get_key_count(line):
    temp = line.strip().split(' ')
    try:
        if temp[1] == None or temp[1] == "" or temp[1] == "\n":
            pass
        else:
            return temp 
    except IndexError:
        pass

# Open the frequency file for bag of words model
text = open('training_freq.txt').read().split('\n')
frequent_words = map(get_key, text)

# Now create a vector for each file
folders = glob.glob("*.folder")
files = glob.glob(folders[1] + '/*')

text = open(files[1]).read().split('\n')
lines = map(get_key_count, text)
lines = filter(None, lines)

# Given the frequency vectors of a document, this computes a BOW for it
def BOW(frequency_vectors):
    word_count = []
    for vector in frequency_vectors:
        if vector[1] in frequent_words:
            word_count.append(0)
        else:
            word_count.append(int(vector[0]))
    return word_count

vec = BOW(lines)
