# Sudoku-Solver-Python
A program that solves n by n Sudoku puzzles using a recursive algorithm.

## Technologies
Project is created with:
* Python version: 3.8.8

## Setup
To run the program first write an input file formatted in the way that's explained below. Then simply type the following command:
```
python3 sudoku_solver.py
```

### Input
The program takes as an input a text file named `puzzle.txt` that contains an unsolved Sudoku puzzle. The puzzle should be given as rows of numbers separated by spaces and missing values should be inputted as zeros. Below is an example of the contents of the file `puzzle.txt` for a 3 by 3 Sudoku puzzle:
```
1 0 0 5 0 3 0 0 0
0 0 9 2 0 4 1 0 3
3 0 0 8 0 0 0 2 4
0 0 0 0 0 6 0 0 0
2 5 0 0 0 0 0 4 6
0 0 0 3 0 0 0 0 0
8 6 0 0 0 7 0 0 5
4 0 3 6 0 5 7 0 0
0 0 0 1 0 9 0 0 8
```

### Output
If the puzzle is solvable, the solution will be stored in a file named `solution.txt`. It will be formatted the same way as `puzzle.txt` but now the zeros have been replaced by right numbers. Below is the contents of the file `solution.txt` corresponding to the the input `puzzle.txt`:
```
1 4 2 5 7 3 6 8 9
5 8 9 2 6 4 1 7 3
3 7 6 8 9 1 5 2 4
9 3 8 7 4 6 2 5 1
2 5 7 9 1 8 3 4 6
6 1 4 3 5 2 8 9 7
8 6 1 4 2 7 9 3 5
4 9 3 6 8 5 7 1 2
7 2 5 1 3 9 4 6 8
```
