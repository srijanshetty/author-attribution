import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = [[] for i in range(numClusters)]
y = [[] for i in range(numClusters)]
z = [[] for i in range(numClusters)]

plt.close('all') # close all latent plotting windows
fig1 = plt.figure() # Make a plotting figure

ax = Axes3D(fig1) # use the plotting figure to create a Axis3D object.

i = -1
for item in pcaVectors.Y:
    i = i + 1
    if i < measurements["sarat"]["number"]:
        x[0].append(item[0])
        y[0].append(item[1])
        z[0].append(item[2])
    elif i < measurements["sarat"]["number"] + measurements["vibhuti"]["number"]:
        x[1].append(item[0])
        y[1].append(item[1])
        z[1].append(item[2])
    elif i < measurements["sarat"]["number"] + measurements["vibhuti"]["number"] + measurements["prem"]["number"]:
        x[2].append(item[0])
        y[2].append(item[1])
        z[2].append(item[2])
    else:
        x[3].append(item[0])
        y[3].append(item[1])
        z[3].append(item[2])

pltData = [x[0],y[0],z[0]] 
ax.scatter(pltData[0], pltData[1], pltData[2], c='b') # make a scatter plot of blue dots from the data

pltData = [x[1],y[1],z[1]] 
ax.scatter(pltData[0], pltData[1], pltData[2], c='g') # make a scatter plot of blue dots from the data

pltData = [x[2],y[2],z[2]] 
ax.scatter(pltData[0], pltData[1], pltData[2], c='r') # make a scatter plot of blue dots from the data

pltData = [x[3],y[3],z[3]] 
ax.scatter(pltData[0], pltData[1], pltData[2], c='y') # make a scatter plot of blue dots from the data
 
# make simple, bare axis lines through space:
xAxisLine = ((min(pltData[0]), max(pltData[0])), (0, 0), (0,0)) # 2 points make the x-axis line at the data extrema along x-axis 
ax.plot(xAxisLine[0], xAxisLine[1], xAxisLine[2], 'k') # make a red line for the x-axis.
yAxisLine = ((0, 0), (min(pltData[1]), max(pltData[1])), (0,0)) # 2 points make the y-axis line at the data extrema along y-axis
ax.plot(yAxisLine[0], yAxisLine[1], yAxisLine[2], 'k') # make a red line for the y-axis.
zAxisLine = ((0, 0), (0,0), (min(pltData[2]), max(pltData[2]))) # 2 points make the z-axis line at the data extrema along z-axis
ax.plot(zAxisLine[0], zAxisLine[1], zAxisLine[2], 'k') # make a red line for the z-axis.
 
# label the axes 
ax.set_xlabel("x-axis label") 
ax.set_ylabel("y-axis label")
ax.set_zlabel("y-axis label")
ax.set_title("The title of the plot")
plt.show() # show the plot
