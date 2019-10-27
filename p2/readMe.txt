
Solving CSPs

In this project, you are expected to solve the following puzzles using a CSP solver.
Although Google OR Tools is highly recommended, you are free to use any CSP
solver.

OR-Tools provides two solvers for constraint programming:

-The CP-SAT solver
-The original CP solver

We used CP-SAT solver. The CP-SAT solver is technologically superior to the original CP solver and should be preferred in almost all situations. The exceptions are small problems for which solutions can be found quickly using either solver. In those cases you may find that the original CP solver outperforms CP-SAT.

● Kakuros
● Futoshiki

Kakuros

Figure below illustrates a simple Kakuros puzzle, solution of the puzzle, input file and
the output file.

input
22, 18, 7
20, 19, 8

output
x, 22, 18, 7
20, 9, 7, 4
19, 8, 9, 2
8, 5, 2,

Futoshiki

Figure below illustrates a simple Futoshiki puzzle, solution of the puzzle, input file and
the output file.

input
B2, 1
D4, 2
A1, A2
A4, B4
C2, C1
D2, D1

output
3, 2, 1, 4
4, 1, 2, 3
2, 3, 4, 1
1, 4, 3, 2


Resoruce ;
https://developers.google.com/optimization/cp
