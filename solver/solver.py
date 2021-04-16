def eliminate_illegal(grid):
    """
    Checks every cell and removes the not valid numbers
    from that cell's possible numbers.
    Goes through checks for box, row and column.
    """
    for row in range(9):
        for col in range(9):
            cell = grid.grid[row][col]
            if cell.is_solved is True:
                continue
            eliminate_boxes(
                grid=grid,
                cell=cell,
                row=row,
                col=col)
            eliminate_rows(
                grid=grid,
                cell=cell,
                row=row
            )
            eliminate_cols(
                grid=grid,
                cell=cell,
                col=col
            )


def eliminate_boxes(grid, cell, row, col):
    nums_to_be_removed = []
    valid_nums = cell.possible_numbers
    for num in valid_nums:
        box_result = grid.check_box(
            number=num,
            row=row,
            col=col
        )
        if box_result is False:
            nums_to_be_removed.append(num)
    for num in nums_to_be_removed:
        cell.possible_numbers.remove(num)


def eliminate_rows(grid, cell, row):
    nums_to_be_removed = []
    valid_nums = cell.possible_numbers
    for num in valid_nums:
        row_result = grid.check_row(
            number=num,
            row=row
        )
        if row_result is False:
            nums_to_be_removed.append(num)
    for num in nums_to_be_removed:
        cell.possible_numbers.remove(num)


def eliminate_cols(grid, cell, col):
    nums_to_be_removed = []
    valid_nums = cell.possible_numbers
    for num in valid_nums:
        col_result = grid.check_column(
            number=num,
            col=col
        )
        if col_result is False:
            nums_to_be_removed.append(num)
    for num in nums_to_be_removed:
        cell.possible_numbers.remove(num)


def find_one_possible_number(grid) -> tuple:
    for row in range(9):
        for col in range(9):
            cell = grid.grid[row][col]
            if cell.is_solved is True:
                continue
            if len(cell.possible_numbers) == 1:
                return (row, col, cell.possible_numbers[0])
    return (-1, -1, -1)


def find_unique_possible_number_in_box(grid, row, col) -> tuple:
    box_cells = grid.get_box_cells(row, col)
    not_solved_cells = []
    for cell in box_cells:
        if cell.is_solved:
            continue
        not_solved_cells.append(cell)
    valid_dict = {}
    for cell in not_solved_cells:
        for num in cell.possible_numbers:
            if num in valid_dict:
                valid_dict[num] += 1
            else:
                valid_dict[num] = 1
    unique_possible_number = 0
    for num in valid_dict:
        if valid_dict[num] == 1:
            unique_possible_number = num
    if unique_possible_number == 0:
        return (-1, -1, -1)
    for cell in not_solved_cells:
        if unique_possible_number in cell.possible_numbers:
            return (cell.position[0], cell.position[1], unique_possible_number)
    return (-1, -1, -1)


def solve_eliminate(grid):
    if grid.solved_count == 81:
        return True
    eliminate_illegal(grid)
    result = find_one_possible_number(grid)
    if result == (-1, -1, -1):
        return False
    grid.grid[result[0]][result[1]].number = result[2]
    grid.solve_cell(result[0], result[1])
    try:
        return solve_eliminate(grid)
    except RecursionError:
        return False


def solve_unique_possible(grid):
    if grid.solved_count == 81:
        return True
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            cell = find_unique_possible_number_in_box(grid, row, col)
            if cell == (-1, -1, -1):
                continue
            grid.grid[cell[0]][cell[1]].number = cell[2]
            grid.solve_cell(cell[0], cell[1])
    try:
        return solve_unique_possible(grid)
    except RecursionError:
        return False


def solve_flow(grid, prev_grid=[]):
    print("Using eliminate method...")
    solve_eliminate_result = solve_eliminate(grid)
    print(grid.solved_count)
    if solve_eliminate_result is True:
        return True
    print("Using unique number in box method...")
    solve_unique_result = solve_unique_possible(grid)
    print(grid.solved_count)
    if solve_unique_result is True:
        return True
    if prev_grid == grid.grid:
        return False
    prev_grid = grid.grid
    try:
        return solve_flow(grid, prev_grid)
    except RecursionError:
        return False
