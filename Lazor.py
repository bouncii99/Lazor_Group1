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
    """ Reads through the .bff file """
    grid = []
    reflect_blocks = []
    opaque_blocks = []
    refract_blocks = []
    lasers = []
    points = []
    in_grid = False
    raw_lines = open(filename, 'r')
    for index, line in enumerate(raw_lines):
        if "GRID STOP" in line:
            in_grid = False
        if in_grid:
            line = line.replace(" ", "")
            grid.append(list(line.strip("\n")))
        if "GRID START" in line:
            in_grid = True
        if line[0] == "A":
            reflect_blocks = [int(s) for s in line if s.isdigit()]
        elif line[0] == "B":
            opaque_blocks = [int(s) for s in line if s.isdigit()]
        elif line[0] == "C":
            refract_blocks = [int(s) for s in line if s.isdigit()]
        if line[0] == "L":
            lasers.append([int(s) for s in re.findall(r'-?\d', line)])
        if line[0] == "P":
            points.append([int(s) for s in line if s.isdigit()])
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
