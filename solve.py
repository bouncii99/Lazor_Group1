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
    print(grid)
    # Initialize blocks by placing them randomly on the board
    Board.generate_board(grid, grid.blocks)
    print(grid)
    # Initialize whatever is necessary to initialize
    # while(all_positions != Filled):
    	# move blocks to a new random positions along with the following criteria:
            # The origsinal lasers must intersect with one of the blocks
            # The positions cannot have been tested already
            # If in the previous position, a laser is being reflected/refracted, keep that block in the same position and only randomly move the other blocks
    	# Refresh board

if __name__ == "__main__":
	# Input file name
    fptr = "dark_1.bff"
    solve(fptr)
