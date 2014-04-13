# A simple PCA of the data, needs a vector called vectors to
# implement the PCA routine

# Needs: vectors

import numpy as np
from matplotlib.mlab import PCA
matrixData = np.array(vectors)
pcaVectors = PCA(matrixData)

