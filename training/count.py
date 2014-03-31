numClusters = 4

# compute precision and recall
measurements = {
        "sarat": {
            "cluster": 0, "recall": 0, "precision": 0, "number": 250, "count" : [0 for x in range(numClusters + 1)]},
        "vibhuti": {"cluster": 0, "recall": 0, "precision": 0, "number": 250, "count" : [0 for x in range(numClusters + 1)]},
        "prem": {"cluster": 0, "recall": 0, "precision": 0, "number": 250, "count" : [0 for x in range(numClusters + 1)]},
        "dharamvir" : {"cluster": 0, "recall": 0, "precision": 0, "number": 250, "count" : [0 for x in range(numClusters + 1)]}
        }

totalSnippets = 0
for key in measurements.keys():
    totalSnippets = totalSnippets + measurements[key]["number"]

for i in range(totalSnippets):
    if i < measurements["sarat"]["number"]:
        for j in range(1, numClusters+1):
            if clusters[i] == j:
                measurements["sarat"]["count"][j] = measurements["sarat"]["count"][j] + 1
    elif i < measurements["sarat"]["number"] + measurements["sarat"]["number"]:
        for j in range(1, numClusters+1):
            if clusters[i] == j:
                measurements["vibhuti"]["count"][j] = measurements["vibhuti"]["count"][j] + 1
    elif i < measurements["sarat"]["number"] + measurements["vibhuti"]["number"] + measurements["prem"]["number"]:
        for j in range(1, numClusters+1):
            if clusters[i] == j:
                measurements["prem"]["count"][j] = measurements["prem"]["count"][j] + 1
    else:
        for j in range(1, numClusters+1):
            if clusters[i] == j:
                measurements["dharamvir"]["count"][j] = measurements["dharamvir"]["count"][j] + 1

# computing the ratios
for key in measurements.keys():
    measurements[key]["countRatio"] = [0 for x in range(numClusters + 1)]
    for i in range(1, numClusters + 1):
        measurements[key]["countRatio"][i] = measurements[key]["count"][i]/measurements[key]["number"]

# find the cluster for each author
for key in measurements.keys():
    l = list(measurements[key]["count"])
    l.sort()
    cluster = l[0]
    measurements[key]["cluster"] = cluster

# compute precision and recall
def computeValues():
    for key in measurements.keys():
        cluster = measurements[key]["cluster"]
        measurements[key]["recall"] = measurements[key]["count"][cluster]/measurements[key]["number"]

        falsePositive = 0
        for j in range(1, numClusters+1):
            falsePositive = falsePositive + measurements[key]["count"][j]

        measurements[key]["precision"] = measurements[key]["count"][cluster]/falsePositive
