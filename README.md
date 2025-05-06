# T1 Algorithm Optimization Project

Project made for the Algorithm Optimization Project discipline in the Software Engineering course in PUCRS.

The objective is to exercise dinamic programing by solving a problem with rats in a maze.

The maze is always squared (n x n) and in every square there is a number that indicates the amount of food there,
the rats start in the bottom left corner and have to go to the top right corner, the rats can only move to 
North(N), East(E) and Northeast(NE)  directions and each move cost 20, 20 and 10 respectively,
the objective is to find the best path for the rats, the path which they get the most points.

There is three steps described in the project:

1. Make a simple recursion with no memorization to solve the problem (this one is really slow).

2. Apply memorization in the previous recursion.

3. Remove the recursion and fill an array of results (to solve the problem really fast).


### Running the project

first clone the repository:
`git clone https://github.com/GuilhermeGMV/T1OtAlg_ratinhos.git`

then run the file you want (1.py, 2.py or 3.py):
`python "the file you want to run"`

Then this message will appear: `Digite o numero do caso de teste(10,20,30,40,50,60,70):`

Which means: `Type the test case number(10,20,30,40,50,60,70):`

after you type the number and press enter the algorithm will run and when it finishes it will show
the best path possible and the amount of points made with this path.
