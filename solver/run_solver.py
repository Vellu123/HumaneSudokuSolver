import argparse
from solver import solve_flow
from sudoku_grid import Grid, set_puzzle
from pprint import pprint


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        help="Puzzle difficult (easy|medium)",
        default="easy"
    )
    return parser.parse_args()


def set_difficulty(args):
    if args.d == "easy":
        return "easy"
    elif args.d == "medium":
        return "medium"


def main():
    args = parse_arguments()
    grid = Grid()
    difficulty = set_difficulty(args)
    set_puzzle(grid, difficulty=difficulty)
    pprint(grid.grid)
    if solve_flow(grid):
        print("SOLVED!")
    else:
        print("COULD NOT SOLVE :(")
    print(grid.solved_count)
    pprint(grid.grid)


if __name__ == "__main__":
    main()
