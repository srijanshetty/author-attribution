<<<<<<< HEAD
# Corpus
- The corpus contains all of the data extracted [Hindisamay](www.hindisamay.com)

# Scripts
- **doc2txt.zsh**: Converts any doc file to txt file.
- **split-folder.zsh**: Pre-processes a given folder by removing punctuations and
then spilts it into 500 word sized files.
```sh
split-folder corpus/rnt/
```

# Training
- **BOW-uni.py**: Creates Unigram BOW.
- **BOW-bi.py**: Creates Bigram BOW.
- **BOW-tri.py**: Creates Trigram BOW.
- **cluster.py**: Clusters a clusterVectors array into 4 clusters.
- **count.py**: For a given clusters array and vectors array, it computers statistics.
- **pca.py**: Performs PCA on a given vectors array
- **plot.py**: Plots first three components of a given pcaVector
- **svm.py**: Performs SVM on a data matrix X and label vector y.
- **unsupervised.py**: Runs the unsupervised learning on a given vectors array.
- **dharamvir_svm.py, prem_svm.py, sarat_svm.py, vibhuti_svm.py**: Performs SVM on them.

# Supervised Learing
- First we create a feature matrix on the training set and a corresponding value matrix
- We perform SVM on this testing data matrix
- Then we test the perdiction of the SVM on the test set.

# Unsupervised learning

## Bigram/Trigram
- Preprocess:
    - Remove unwanted characters.
    - create snippets of 500 words each.
- Count the number of ngram in the corpus and determine the top 2000 ngrams
- Create a BOW for each of the snippet using these top 2000 ngrams.
- Perform PCA on these BOW to get 20 dimensional vectors.
- Apply K means clustering with 4 means on these vectors.
- Use the ground-truth to determine the validity using precision and recall.

## Combined bigram and trigram
- Preprocess:
    - Remove unwanted characters.
    - create snippets of 500 words each.
- Perfrom bigram and trigram on the corpus to obtain top 1000 grams.
- Create a BOW for each snippet using these two feature sets.
- Perform PCA on these BOW to get 20 dimensional vectors.
- Apply K means clustering with 4 means on these vectors.
- Use the ground-truth to determine the validity using precision and recall.

# Sources
- [Code Snippets](http://www.csc.villanova.edu/~matuszek/spring2012/snippets.html)


