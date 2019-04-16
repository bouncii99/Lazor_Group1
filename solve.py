"""
Solving algorithm
"""
import read
from lazor import Board


def try_solution(grid, list_of_incorrect_boards):
    while True:
        x, _ = Board.generate_board(grid, grid.blocks)
        print(x)
        if x not in list_of_incorrect_boards:
            break
    y, _ = Board.refresh_lasers(x)
    return y


def solve(filename):
    # Read and parse through board file
    g, rflb, ob, rfrb, l, p = read.read_bff(filename)
    # Initialize board class
    grid = Board(g, l, p, rflb, ob, rfrb)
    print("--- Initial grid ---")
    print(repr(grid))
    print("\n")
    incorrect_boards = []
    while True:
        # Place blocks randomly on the board and refresh lasers
        print("Trying solutions...")
        test = try_solution(grid, incorrect_boards)
        if Board.check_solution(test):
            break
        else:
            incorrect_boards.append(test)
    print("Solution has been found!")


if __name__ == "__main__":
    # Input file name
    file = "mad_4.bff"
    solve(file)
