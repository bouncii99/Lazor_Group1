"""
Solving algorithm
"""
import read
from lazor import Board
import re
from textwrap import wrap


def try_solution(grid):
    x, _ = Board.generate_board(grid)
    Board.refresh_lasers(x)


def solve(filename):
    # Read and parse through board file
    g, rflb, ob, rfrb, L, p = read.read_bff(filename)
    # Initialize board class
    board = Board(g, L, p, rflb, ob, rfrb)
    # incorrect_boards = []
    count = 0
    while True:
        # Place blocks randomly on the board and refresh lasers
        try_solution(board)
        if Board.check_solution(board):
            solution = str(board.grid)
            break
        else:
            del board
            g, rflb, ob, rfrb, L, p = read.read_bff(filename)
            board = Board(g, L, p, rflb, ob, rfrb)
            count += 1
    return solution


def board_display(output, filename):
    board_name, _ = filename.split(".")
    sol_file = open(board_name + "_solution.txt", "w")
    sol_file.write("Solution for " + board_name + ":\n")
    cleanstring = re.sub('\W+', "", output)
    cleanstring_grid = wrap(cleanstring, int(len(cleanstring) ** 0.5))
    new_strings = []
    for i, j in enumerate(cleanstring_grid):
        new_strings.append(" ".join(j))
    for i in new_strings:
        sol_file.write("%s\n" % i)


if __name__ == "__main__":
    # Input test cases
    files = ["dark_1.bff", "mad_1.bff", "mad_4.bff",
             "mad_7.bff", "numbered_6.bff", "showstopper_4.bff",
             "tiny_5.bff", "yarn_5.bff"]
    for file in files:
        output = solve(file)
        board_display(output, file)
