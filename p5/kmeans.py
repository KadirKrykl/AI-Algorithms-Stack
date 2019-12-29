#import libraries
import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

data = pd.read_csv('data.csv')

X = data[["INCOME","SPEND"]]
#Visualise data points
plt.scatter(X["INCOME"],X["SPEND"],c='black')
plt.xlabel('Income')
plt.ylabel('Spend')



with PdfPages(r'plot.pdf') as export_pdf:
    
    for K in range(2,6):

        # Select random observation as centroids
        Centroids = (X.sample(n=K))
        plt.scatter(X["INCOME"],X["SPEND"],c='black')
        plt.scatter(Centroids["INCOME"],Centroids["SPEND"],c='red')
        plt.xlabel('Income')
        plt.ylabel('Spend')

        diff = 1
        j=0

        while(diff!=0):
            XD=X
            i=1
            for index1,row_c in Centroids.iterrows():
                ED=[]
                for index2,row_d in XD.iterrows():
                    d1=(row_c["INCOME"]-row_d["INCOME"])**2
                    d2=(row_c["SPEND"]-row_d["SPEND"])**2
                    d=np.sqrt(d1+d2)
                    ED.append(d)
                X[i]=ED
                i=i+1

            C=[]
            for index,row in X.iterrows():
                min_dist=row[1]
                pos=1
                for i in range(K):
                    if row[i+1] < min_dist:
                        min_dist = row[i+1]
                        pos=i+1
                C.append(pos)
            X["Cluster"]=C
            Centroids_new = X.groupby(["Cluster"]).mean()[["SPEND","INCOME"]]
            if j == 0:
                diff=1
                j=j+1
            else:
                diff = (Centroids_new['SPEND'] - Centroids['SPEND']).sum() + (Centroids_new['INCOME'] - Centroids['INCOME']).sum()
                print(diff.sum())
            Centroids = X.groupby(["Cluster"]).mean()[["SPEND","INCOME"]]

        color=['blue','green','cyan','gray','purple']
        for k in range(K):
            data=X[X["Cluster"]==k+1]
            plt.scatter(data["INCOME"],data["SPEND"],c=color[k])
        plt.scatter(Centroids["INCOME"],Centroids["SPEND"],c='red')
        plt.xlabel('Income')
        plt.ylabel('Spend')
        plt.title("K = {}".format(K))
        export_pdf.savefig()
        plt.close()


