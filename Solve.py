"""
Solving algorithm
"""
import Lazor

def main():
    # Input file name
    fptr = "mad_1.bff"
    # Read and parse through board file
    g, rflb, ob, rfrb, l, p = Read.read_bff(fptr)
    # Make an instance of the board object and save it in a variable
    grid = Board(g)
    # Make instances of all blocks
    reflect_blocks, opaque_blocks, refract_blocks = [], [], []
    for i in range(rflb):
        reflect_blocks.append(Block("A"))
    for i in range(ob):
        opaque_blocks.append(Block("B"))
    for i in range(rfrb):
        refract_blocks.append(Block("C"))
    # Make instances of the lasers
    lasers = []
    for i in l:
        lasers.append(Laser(i))
    # Make instances of the points
    points = []
    for i in p:
        points.append(i)
    return grid, reflect_blocks, opaque_blocks, refract_blocks, lasers, points


def solve(board):
    # From the blocks that are available, place them in random spots on the
    # board
	# INPUT FUNCTION/CODE TO PLACE BLOCKS HERE
    # Initialize whatever is necessary to initialize
    # while(all_positions != Filled):
    	# move blocks to a new random positions
    	# Refresh board
	"""
	pass

if __name__ == "__main__":
	print(Lazor.read_bff("mad_1.bff"))
