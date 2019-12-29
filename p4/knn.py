import pandas as pd
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time

dataTest= pd.read_csv("test.csv")

f= open("train.csv","r")
dataTrainDict={}
c=0
a=True
for i in f:
    if(a):
        a=False
        continue
    dataTrainDict[c]=[float(x) for x in i[:-1].split(",")]
    dataTrainDict[c]
    c+=1

def classifyDict(trainSet,test,k):
    distances={}
    for i in range(0,len(trainSet)):
        distances[i]=math.sqrt((trainSet[i][0]-test[0])**2+(trainSet[i][1]-test[1])**2+(trainSet[i][2]-test[2])**2+(trainSet[i][3]-test[3])**2+(trainSet[i][4]-test[4])**2+(trainSet[i][5]-test[5])**2+(trainSet[i][6]-test[6])**2+(trainSet[i][7]-test[7])**2+(trainSet[i][8]-test[8])**2+(trainSet[i][9]-test[9])**2+(trainSet[i][10]-test[10])**2+(trainSet[i][11]-test[11])**2+(trainSet[i][12]-test[12])**2+(trainSet[i][13]-test[13])**2+(trainSet[i][14]-test[14])**2+(trainSet[i][15]-test[15])**2+(trainSet[i][16]-test[16])**2+(trainSet[i][17]-test[17])**2+(trainSet[i][18]-test[18])**2+(trainSet[i][19]-test[19])**2)
    sortedDistance= {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
    freqs=[0,0,0,0]
    k2=0
    for i in sortedDistance.keys():
        if trainSet[i][20]==0:
            freqs[0]+=1
        elif trainSet[i][20]==1:
            freqs[1]+=1
        elif trainSet[i][20]==2:
            freqs[2]+=1
        elif trainSet[i][20]==3:
            freqs[3]+=1
        k2+=1
        if k2==k:
            break
    maxC=max(freqs)
    return freqs.index(maxC)


rowCountTest=len(dataTest)

accuracy={}
priceRangeList = dataTest["price_range"].tolist()

for k in range(1,11):
    #Classify Section
    resultsDict={}
    for i in range(0,rowCountTest):
        start_time = time.time()
        resultsDict[i]= 1 if priceRangeList[i]==classifyDict(dataTrainDict,dataTest.iloc[i].tolist(),k) else 0
        elapsed_time = time.time() - start_time
        print("{0} => {1}".format(i,elapsed_time))

    #Accurracy Calculation
    count=0
    for value in resultsDict.values():
        if value==1:
            count+=1
    accuracy[k]=(count/rowCountTest)*100

labels = ['1', '2', '3', '4', '5','6','7','8','9','10']
accurracy = accuracy.values()

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x, accurracy, width,label="Accuracy")
ax.set_ylabel('Accuracy')
ax.set_title('Accuracy by k')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_xlabel('K')
ax.legend(loc=8)
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
fig.tight_layout()
plt.savefig("plot.pdf")