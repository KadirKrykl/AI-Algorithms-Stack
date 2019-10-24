from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model

inputFile=open("kakuro_input.txt", "r")

model = cp_model.CpModel() #define model for problem

#Variables

x1 = model.NewIntVar(1, 9, 'x1')
x2 = model.NewIntVar(1, 9, 'x2')
x3 = model.NewIntVar(1, 9, 'x3')
y1 = model.NewIntVar(1, 9, 'y1')
y2 = model.NewIntVar(1, 9, 'y2')
y3 = model.NewIntVar(1, 9, 'y3')
z1 = model.NewIntVar(1, 9, 'z1')
z2 = model.NewIntVar(1, 9, 'z2')
z3 = model.NewIntVar(1, 9, 'z3')

#ALLDIFF
diffRow1=[x1,x2,x3]
diffRow2=[y1,y2,y3]
diffRow3=[z1,z2,z3]

diffCol1=[x1,y1,z1]
diffCol2=[x2,y2,z2]
diffCol3=[x3,y3,z3]

model.AddAllDifferent(diffRow1)
model.AddAllDifferent(diffRow2)
model.AddAllDifferent(diffRow3)

model.AddAllDifferent(diffCol1)
model.AddAllDifferent(diffCol2)
model.AddAllDifferent(diffCol3)



mydict={}
i=0
for line in inputFile:
    lineArray=line.split(", ")
    if "\n" in lineArray[2]:
        lineArray[2]=lineArray[2][:-1]
    mydict[i]=lineArray
    i=i+1
print(mydict)
print(mydict[0][0])
#Constraints continue
model.Add(x1+x2+x3==int(mydict[1][0]))
model.Add(y1+y2+y3==int(mydict[1][1]))
model.Add(z1+z2+z3==int(mydict[1][2]))

model.Add(x1+y1+z1==int(mydict[0][0]))
model.Add(x2+y2+z2==int(mydict[0][1]))
model.Add(x3+y3+z3==int(mydict[0][2]))

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE:
    fileOutput=open("kakuro_output.txt", "w+")
    fileOutput.write("x, {0}, {1}, {2}\n".format(mydict[0][0],mydict[0][1],mydict[0][2]))
    fileOutput.write("{0}, {1}, {2}, {3}\n".format(mydict[1][0],solver.Value(x1),solver.Value(x2),solver.Value(x3)))
    fileOutput.write("{0}, {1}, {2}, {3}\n".format(mydict[1][1],solver.Value(y1),solver.Value(y2),solver.Value(y3)))
    fileOutput.write("{0}, {1}, {2}, {3}".format(mydict[1][2],solver.Value(z1),solver.Value(z2),solver.Value(z3)))
    fileOutput.close()