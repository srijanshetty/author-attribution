import nltk
from nltk import cluster
from nltk.cluster import util
from nltk.cluster import api
from nltk.cluster import euclidean_distance
from nltk.cluster import cosine_distance
from nltk.cluster import KMeansClusterer

clusterer = KMeansClusterer(5, cosine_distance)
clusters = clusterer.cluster(vectors, assign_clusters=True, trace=False)
means = clusterer.means()
