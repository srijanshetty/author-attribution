# Analysis of the SVM that was performed on vibhuti

# For vibhuti we take 702 to 1002, i.e, 300 correct samples
# Wrong ones 0:500 1202:1702, i.e., 900 incorrect samples
# so we have 1500 data points

# The steps are

# Create the data
X = vectors[702:1002]
X.extend(vectors[1202:1502])
X.extend(vectors[1802:1902])
X.extend(vectors[:500])

y = []
for i in range(1200):
    if i < 300:
        y.append(1)
    else:
        y.append(0)

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
    elif i < 702: # 500, 701
        if results[i]:
            count['FP'] += 1
        else:
            count['TN'] += 1
    elif i < 1002: # 702, 1001
        pass
    elif i < 1181: # 1002, 1180
        if results[i]:
            count['TP'] += 1
        else:
            count['FN'] += 1
    elif i < 1202: # 1181, 1201
        if results[i]:
            count['FP'] += 1
        else:
            count['TN'] += 1
    elif i < 1502: # 1202, 1501
        pass
    elif i < 1802: # 1502, 1801
        if results[i]:
            count['FP'] += 1
        else:
            count['TN'] += 1
    elif i < 1902: # 1802, 1901
        pass
    else: # 1902, 2088
        if results[i]:
            count['FP'] += 1
        else:
            count['TN'] += 1
