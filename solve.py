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
    # Initialize blocks by placing them randomly on the board
    for i in grid.blocks:
        Board.random_placement(grid, i)
    print(grid)
    #Board.random_placement(grid, )
    # From the blocks that are available, place them in random spots on the
    # board
	# INPUT FUNCTION/CODE TO PLACE BLOCKS HERE
    # Initialize whatever is necessary to initialize
    # while(all_positions != Filled):
    	# move blocks to a new random positions along with the following criteria:
            # The original lasers must intersect with one of the blocks
            # The positions cannot have been tested already
            # If in the previous position, a laser is being reflected/refracted, keep that block in the same position and only randomly move the other blocks
    	# Refresh board

if __name__ == "__main__":
	# Input file name
    fptr = "yarn_5.bff"
    solve(fptr)
