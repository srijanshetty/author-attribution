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



