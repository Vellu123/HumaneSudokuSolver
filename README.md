# A Sudoku solver using humanlike methods

I wanted to try to create a sudoku solver which uses the same scanning methods we humans use.
Currently the solver eliminates illegal moves and scans for cells which have just one solution.
These techniques can solve easy and some medium sudoku puzzles.

### Usage
1. Clone repo
1. Depending on the puzzle, run either one:
    1. `python run_solver.py -d easy`
    1. `python run_solver.py -d medium`

### Methods
The solver has the following flow:
1. `solve_eliminate()`: Recursively looks for cells with only one possible move by eliminating illegal moves (no same number in a row, column or box)
2. `solve_unique_possible()`: In a box with multiple unsolved cells, this method checks at the cells' possible moves, and if there is a possible move which can only be done in one cell, we have found a solution.