# Analysis of the SVM that was performed on sarat

# For sarat we take 0 to 499, i.e, 500 correct samples
# Then 702 to 1352, i.e., 650 more incorrect
# Then 1802 to 1952, i.e., 150 more incorrect

# The steps are

# Create the data
X = vectors[:500]
X.extend(vectors[702:1352])
X.extend(vectors[1802:1952])

y = []
for i in range(1300):
    if i < 500:
        y.append(1)
    else:
        y.append(0)

# Apply SVm
from sklearn import svm
clf = svm.SVC()
clf.fit(X, y)
results = clf.predict(vectors)

# Count results
count = {'TP' : 0, 'FP': 0, 'TN': 0, 'FN':0 }
for i in range(2089):
    if i < 500: # 0, 499
        pass
    elif i < 702: # 500, 701
        if results[i]:
            count['TP'] += 1
        else:
            count['FN'] += 1
    elif i < 1352: # 702, 1351
        pass
    elif i < 1802: # 1352, 1801
        if results[i]:
            count['FP'] += 1
        else:
            count['TN'] += 1
        pass
    elif i < 1952: # 1802, 1951
        pass
    else: # 1952, 2088
        if results[i]:
            count['FP'] += 1
        else:
            count['TN'] += 1
        pass
