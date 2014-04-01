import nltk
from nltk import cluster
from nltk.cluster import util
from nltk.cluster import api
from nltk.cluster import euclidean_distance
from nltk.cluster import cosine_distance
from nltk.cluster import KMeansClusterer

numClusters = 4
print "KMeans Clustering with %d means and using cosine distance" %numClusters
clusterer = KMeansClusterer(numClusters, cosine_distance)
clusters = clusterer.cluster(vectors, assign_clusters=True, trace=False)
means = clusterer.means()
