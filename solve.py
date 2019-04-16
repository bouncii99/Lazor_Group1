"""
Solving algorithm
"""
import read
from lazor import Board


def solve(filename):
    # Read and parse through board file
    g, rflb, ob, rfrb, l, p = read.read_bff(filename)
    # Initialize board class
    grid = Board(g, l, p, rflb, ob, rfrb)
    print("--- Initial grid ---")
    print(repr(grid))
    print("\n")
    # Place blocks randomly on the board and refresh lasers
    Board.generate_board(grid, grid.blocks)
    Board.refresh_lasers(grid)
    print("--- Place blocks and refresh lasers---")
    print(repr(grid))
    print(Board.check_solution(grid))
    print("\n")


if __name__ == "__main__":
    # Input file name
    file = "mad_4.bff"
    solve(file)
