# Analysis of the SVM that was performed on Dharamvir

# Wrong ones 0:500 1000:1500, i.e., 1000 incorrect samples
# Right ones are 1839:2039, i.e, 200 correct samples

# The steps are

# Create the data
X = vectors[:500] # 500 false
X.extend(vectors[1000:1500]) # 500 false 
X.extend(vectors[1839:2039]) # 200 true 

y = []
for i in range(1200):
    if i < 1000:
        y.append(0)
    else:
        y.append(1)

# Apply SVM
from sklearn import svm
clf = svm.SVC()
clf.fit(X, y)
results = clf.predict(vectors)

# Count the results
count = {'TP' : 0, 'FP': 0, 'TN': 0, 'FN':0 }
for i in range(2089):
    if i < 500: # 0, 499
        pass
    elif i < 1000: # 500, 1000
        if results[i]:
            count['FP'] += 1
        else:
            count['TN'] += 1
    elif i < 1500: # 1000, 1500
        pass
    elif i < 1839: # 1500, 1838
        if results[i]:
            count['FP'] += 1
        else:
            count['TN'] += 1
    elif i < 2039: #1839, 2038
        pass
    else: # 2039, 2088
        if results[i]:
            count['TP'] += 1
        else:
            count['FN'] += 1
