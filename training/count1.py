numClusters = 5

# compute precision and recall
measurements = {
        "rnt" : {"cluster": 0, "recall": 0, "precision": 0, "number":151, "count" : [0,0,0,0,0,0] },
        "dharamvir" : {"cluster": 0, "recall": 0, "precision": 0, "number": 201, "count" : [0,0,0,0,0,0]},
        "sarat": {"cluster": 0, "recall": 0, "precision": 0, "number": 542, "count" : [0,0,0,0,0,0]},
        "vibhuti": {"cluster": 0, "recall": 0, "precision": 0, "number": 418, "count" : [0,0,0,0,0,0]},
        "prem": {"cluster": 0, "recall": 0, "precision": 0, "number": 398, "count" : [0,0,0,0,0,0]}
        }

for i in range(1710):
    if i < 151:
        for j in range(1, numClusters+1):
            if clusters[i] == j:
                measurements["rnt"]["count"][j] = measurements["rnt"]["count"][j] + 1
    elif i < 693:
        for j in range(1, numClusters+1):
            if clusters[i] == j:
                measurements["sarat"]["count"][j] = measurements["sarat"]["count"][j] + 1
    elif i < 1111:
        for j in range(1, numClusters+1):
            if clusters[i] == j:
                measurements["vibhuti"]["count"][j] = measurements["vibhuti"]["count"][j] + 1
    elif i < 1509:
        for j in range(1, numClusters+1):
            if clusters[i] == j:
                measurements["prem"]["count"][j] = measurements["prem"]["count"][j] + 1
    else:
        for j in range(1, numClusters+1):
            if clusters[i] == j:
                measurements["dharamvir"]["count"][j] = measurements["dharamvir"]["count"][j] + 1

# find the cluster for each author
for i in range(1, numClusters+1):
    for key in measurements.keys():
        cluster = measurements[key]["cluster"]
        if measurements[key]["count"][i] > measurements[key]["count"][cluster]:
            measurements[key]["cluster"] = i

# compute precision and recall
for key in measurements.keys():
    cluster = measurements[key]["cluster"]
    measurements[key]["recall"] = measurements[key]["count"][cluster]/measurements[key]["number"]

    falsePositive = 0
    for j in range(1, numClusters+1):
        falsePositive = falsePositive + measurements[key]["count"][j]

    measurements[key]["precision"] = measurements[key]["count"][cluster]/falsePositive
