

K-means Clustering

K-means clustering is one of the simplest and popular unsupervised machine learning algorithms.
Typically, unsupervised algorithms make inferences from datasets using only input vectors without referring to known, or labelled, outcomes.


Source file: kmeans.py
Input file: data.csv
Output file: plot.pdf

How is it Work

First, he chooses random centers as many as the number K.
The distance of these centers to the points in the data.csv file is calculated and the points close to the center are added to that group.
After all points are added to the groups, the centers are recentered according to the locations of their points.
after this event, if a point is close to another center, it is added to the nearest center.
Finally, the resulting coordinate system is colored and plotted on the graph.

