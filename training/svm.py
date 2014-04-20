#################################################
# SVM routine                                   #
#                                               #
# Requirements: data-matrix(X), labels(y)       #
# Usage       : %loadpy pca.py                  #
#################################################

from sklearn import svm
clf = svm.SVC()
clf.fit(X, y)
results = clf.predict(vectors)
