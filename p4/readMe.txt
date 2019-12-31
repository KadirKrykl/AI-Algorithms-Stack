
KNN Algorithhm

K Nearest Neighbors is a simple algorithm that stores all available cases and classifies new cases based on a similarity measure (e.g., distance functions). 
KNN has been used in statistical estimation and pattern recognition already in the beginning of 1970’s as a non-parametric technique.  


Source file: knn.py
Input files: train.csv, test.csv
Output file: plot.pdf

How is it Work

First of all there are 2 csv files and The files include phones and their features.
It then selects a random phone from the test.csv file. With the selected phone train.csv file to each phone individually with the help of Euclidean form finds distances.
groups the phones in the train.csv file according to the distances found.
Finally, he prints the accuracy of his grouping on the table for each attempt.
