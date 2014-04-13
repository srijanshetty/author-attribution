# Simple pca routine, needs:

# X which is a list of lists storing the vectors
# y which is the corresponding value of the vectors

from sklearn import svm
clf = svm.SVC()
clf.fit(X, y)
results = clf.predict(vectors)
