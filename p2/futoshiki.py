from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model

inputFile=open("futoshiki_input.txt", "r")

model = cp_model.CpModel() #define model for problem

#Variables

A1 = model.NewIntVar(1, 4, 'A1')
A2 = model.NewIntVar(1, 4, 'A2')
A3 = model.NewIntVar(1, 4, 'A3')
A4 = model.NewIntVar(1, 4, 'A4')

B1 = model.NewIntVar(1, 4, 'B1')
B2 = model.NewIntVar(1, 4, 'B2')
B3 = model.NewIntVar(1, 4, 'B3')
B4 = model.NewIntVar(1, 4, 'B4')

C1 = model.NewIntVar(1, 4, 'C1')
C2 = model.NewIntVar(1, 4, 'C2')
C3 = model.NewIntVar(1, 4, 'C3')
C4 = model.NewIntVar(1, 4, 'C4')

D1 = model.NewIntVar(1, 4, 'D1')
D2 = model.NewIntVar(1, 4, 'D2')
D3 = model.NewIntVar(1, 4, 'D3')
D4 = model.NewIntVar(1, 4, 'D4')

#ALLDIFF
diffRow1=[A1,A2,A3,A4]
diffRow2=[B1,B2,B3,B4]
diffRow3=[C1,C2,C3,C4]
diffRow4=[D1,D2,D3,D4]

diffCol1=[A1,B1,C1,D1]
diffCol2=[A2,B2,C2,D2]
diffCol3=[A3,B3,C3,D3]
diffCol4=[A4,B4,C4,D4]

model.AddAllDifferent(diffRow1)
model.AddAllDifferent(diffRow2)
model.AddAllDifferent(diffRow3)
model.AddAllDifferent(diffRow4)

model.AddAllDifferent(diffCol1)
model.AddAllDifferent(diffCol2)
model.AddAllDifferent(diffCol3)
model.AddAllDifferent(diffCol4)


for line in inputFile:
    lineArray=line.split(", ")
    if "\n" in lineArray[1]:
        lineArray[1]=lineArray[1][:-1]
    if lineArray[1].isdigit():
        #exec("%s == %d" % (lineArray[0],int(lineArray[1])))
        model.Add(vars()[lineArray[0]]==int(lineArray[1]))
    else:
        model.Add(vars()[lineArray[0]]>vars()[lineArray[1]])


solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE:
    fileOutput=open("futoshiki_output.txt", "w+")
    fileOutput.write("{0}, {1}, {2}, {3}\n".format(solver.Value(A1),solver.Value(A2),solver.Value(A3),solver.Value(A4)))
    fileOutput.write("{0}, {1}, {2}, {3}\n".format(solver.Value(B1),solver.Value(B2),solver.Value(B3),solver.Value(B4)))
    fileOutput.write("{0}, {1}, {2}, {3}\n".format(solver.Value(C1),solver.Value(C2),solver.Value(C3),solver.Value(C4)))
    fileOutput.write("{0}, {1}, {2}, {3}".format(solver.Value(D1),solver.Value(D2),solver.Value(D3),solver.Value(D4)))
    fileOutput.close()