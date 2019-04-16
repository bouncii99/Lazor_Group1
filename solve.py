"""
Solving algorithm
"""
import read
from lazor import Board


def try_solution(grid, list_of_incorrect_boards):
    while True:
        x, _ = Board.generate_board(grid)
        if x not in list_of_incorrect_boards:
            break
    Board.refresh_lasers(x)


def solve(filename):
    # Read and parse through board file
    g, rflb, ob, rfrb, L, p = read.read_bff(filename)
    # Initialize board class
    board = Board(g, L, p, rflb, ob, rfrb)
    print("--- Initial board ---")
    print(board)
    print("\n")
    incorrect_boards = []
    count = 0
    while True:
        # Place blocks randomly on the board and refresh lasers
        try_solution(board, incorrect_boards)
        if Board.check_solution(board):
            solution = str(board.grid)
            break
        else:
            print(count)
            print(repr(board))
            incorrect_boards.append(board)
            del board
            g, rflb, ob, rfrb, L, p = read.read_bff(filename)
            board = Board(g, L, p, rflb, ob, rfrb)
            count += 1
    print("Solution has been found!")
    print(solution)


if __name__ == "__main__":
    # Input file name
    file = "mad_1.bff"
    solve(file)
