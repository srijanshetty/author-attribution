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
def get_count(line):
    temp = line.strip().split(' ')
    try:
        if temp[1]:
            return temp 
    except IndexError:
        pass

# Open the frequency file for bag of words model
text = open('training_freq.txt').read().split('\n')
ref = map(get_key, text)

# Now create a vector for each file
folders = glob.glob("*.folder")
files = glob.glob(folders[1] + '/*')

text = open(files[1]).read().split('\n')
lines = map(get_count, text)

