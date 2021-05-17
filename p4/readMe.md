

# KNN Algorithhm

K Nearest Neighbors is a simple algorithm that stores all available cases and classifies new cases based on a similarity measure (e.g., distance functions). 
KNN has been used in statistical estimation and pattern recognition already in the beginning of 1970’s as a non-parametric technique.  


**Source file:** knn.py
**Input files:** train.csv, test.csv
**Output file:** plot.pdf

**How is it Work**

 1. There are 2 csv files and The files include phones and their features.
 2. It then selects a random phone from the test.csv file.
 3. With the selected phone train.csv file to each phone individually with the help of Euclidean form finds distances.
 4. Groups the phones in the train.csv file according to the distances found.
 5. Finally, he prints the accuracy of his grouping on the table for each attempt.
