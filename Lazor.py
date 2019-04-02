import re


class Board:
    """
    Board class represents the Lazors game board.
    **Parameters**

        list all parameters that appear in __init__
        rows: ints
        columns: ints
    """

    def __init__(self, rows, columns):
        """ Create new board """
        self.rows = rows
        self.columns = columns

    def __repr__(self):
        """ Representation of the object for debugging """
        pass

    def __str__(self):
        """ String representation of the object """
        pass

    def add_block(self, block_type):
        """ Add a block to the board """
        pass

    def place_block(self):
        """ Place a block at a given position """
        pass

    def laser(self, x, y, vx, vy):
        """ Specify a laser and the direction it is pointing in """
        # Laser can be represented by a system of lines/linear equations
        pass

    def point(self):
        """ Define point where the laser has to intersect """
        pass

    def refresh(self):
        """ Redraw the board once a block has been moved """
        pass


def read_bff(filename):
    """
    Reads and parses through the .bff file.
    **Parameters**
        filename: *str*
            The name of the .bff file to be read.
    **Returns**
        grid: *list, str*
            A list of lists corresponding to the grid from the original .bff
            file. Each list corresponds to a row of the grid and each string
            element corresponds to a spot on the board.
        reflect_blocks: *int*
            The number of reflect blocks available to use to solve the puzzle.
        opaque_blocks: *int*
            The number of opaque blocks available to use to solve the puzzle.
        refract_blocks: *int*
            The number of refract blocks available to use to solve the puzzle.
        lasers: *list, int*
            A list containing the lasers in the puzzle. For each laser, the
            first two integers correspond to the position of the laser and the
            last two integers correspond to the direction it is pointing in.
        points: *list, int*
            A list containing the coordinates of the points where the lasers
            have to intersect to solve the puzzle.
    """
    # Initialize empty lists for the outputs
    grid = []
    reflect_blocks = []
    opaque_blocks = []
    refract_blocks = []
    lasers = []
    points = []
    # Define boolean value to keep track of if the line we are parsing through
    # represents the grid
    in_grid = False
    # Open the file and read through each line
    raw_lines = open(filename, 'r')
    for index, line in enumerate(raw_lines):
        # Parse through the grid portion of the file
        if "GRID STOP" in line:
            in_grid = False
        if in_grid:
            line = line.replace(" ", "")
            grid.append(list(line.strip("\n")))
        if "GRID START" in line:
            in_grid = True
        # Parse through the blocks
        if line[0] == "A":
            reflect_blocks = [int(s) for s in line if s.isdigit()]
        elif line[0] == "B":
            opaque_blocks = [int(s) for s in line if s.isdigit()]
        elif line[0] == "C":
            refract_blocks = [int(s) for s in line if s.isdigit()]
        # Parse through the lasers and intersection points
        if line[0] == "L":
            lasers.append([int(s) for s in re.findall(r'-?\d', line)])
        if line[0] == "P":
            points.append([int(s) for s in line if s.isdigit()])
    # Convert block lists to appropriate ints
    if len(reflect_blocks) > 0:
        reflect_blocks = reflect_blocks[0]
    else:
        reflect_blocks = 0
    if len(opaque_blocks) > 0:
        opaque_blocks = opaque_blocks[0]
    else:
        opaque_blocks = 0
    if len(refract_blocks) > 0:
        refract_blocks = refract_blocks[0]
    else:
        refract_blocks = 0
    return grid, reflect_blocks, opaque_blocks, refract_blocks, lasers, points


if __name__ == "__main__":
    # Input file name
    fptr = "yarn_5.bff"
    # Read and parse through board file
    g, rflb, ob, rfrb, l, p = read_bff(fptr)
    # Make an instance of the board object and save it in a variable
    board_row = len(g)
    board_col = len(g[0])
    board = Board(board_row, board_col)
