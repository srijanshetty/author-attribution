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

# Sources
- [Code Snippets](http://www.csc.villanova.edu/~matuszek/spring2012/snippets.html)


