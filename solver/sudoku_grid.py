from sudoku_cell import Cell
from pprint import pprint


class Grid:
    def __init__(self):
        self.grid = [
            [Cell() for x in range(9)] for y in range(9)
        ]
        self.solved_count = 0
        self.__init_cell_position()

    def __repr__(self):
        return ("Sudoku grid")

    def __init_cell_position(self):
        for row in range(9):
            for col in range(9):
                self.grid[row][col].position = (row, col)

    def solve_cell(self, row, col):
        self.grid[row][col].is_solved = True
        self.solved_count += 1

    def check_solve_status(self) -> int:
        """Return count of cells to be solved"""
        not_solved_count = 81
        for row in range(9):
            for col in range(9):
                if self.grid[row][col].is_solved is True:
                    not_solved_count -= 1
        return not_solved_count

    def check_row(self, number, row) -> bool:
        for cell in self.grid[row]:
            if number == cell.number:
                return False
        return True

    def check_column(self, number, col) -> bool:
        for row in range(9):
            if number == self.grid[row][col].number:
                return False
        return True

    def check_box(self, number, row, col) -> bool:
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if number == self.grid[i][j].number:
                    return False
        return True

    def get_box_cells(self, row, col) -> list:
        cells = []
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                cells.append(self.grid[i][j])
        return cells


def set_puzzle(grid, difficulty="easy"):
    if difficulty == "easy":
        puzzle = [[0, 0, 4, 6, 7, 2, 0, 0, 0],
                  [5, 0, 0, 8, 0, 0, 0, 9, 6],
                  [0, 6, 3, 0, 4, 0, 0, 0, 8],
                  [3, 8, 2, 1, 0, 0, 9, 6, 0],
                  [4, 7, 5, 0, 0, 0, 1, 0, 0],
                  [9, 1, 0, 2, 0, 4, 5, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 2, 9],
                  [0, 0, 1, 0, 0, 0, 7, 4, 3],
                  [2, 0, 0, 0, 6, 3, 8, 0, 1]]
    elif difficulty == "medium":
        puzzle = [[0, 0, 4, 0, 8, 0, 0, 5, 0],
                  [0, 1, 0, 0, 0, 5, 0, 0, 0],
                  [3, 5, 0, 0, 0, 0, 2, 0, 0],
                  [0, 0, 0, 0, 9, 4, 6, 0, 0],
                  [9, 0, 0, 0, 2, 7, 0, 0, 0],
                  [0, 0, 8, 1, 0, 3, 5, 4, 0],
                  [0, 7, 3, 0, 0, 1, 0, 0, 8],
                  [5, 0, 0, 2, 0, 9, 0, 0, 0],
                  [2, 0, 0, 7, 0, 8, 4, 0, 0]]

    for row in range(9):
        for cell in range(9):
            grid.grid[row][cell].number = puzzle[row][cell]
            if puzzle[row][cell] != 0:
                grid.solve_cell(row, cell)


if __name__ == "__main__":
    sudoku_grid = Grid()
    set_puzzle(sudoku_grid)
    pprint(sudoku_grid.grid)
    result = sudoku_grid.check_box(
        number=9,
        row=7,
        col=2
    )
    print(result)
