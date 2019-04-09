import re


class Board(object):
    """
    The Board class represents the entire Lazors game board, including the
    lasers, blocks, and desired intersection points.

    **Parameters**

        grid: *list, str*
            The list of characters that represents all of the available spots
            on the board. Each list inside the list represents a row of the
            board.
        grid_param: *list, boolean*
            A list of True and False parameters corresponding to all of the
            positions on the board. If the grid_param is True, then a block
            can be placed in that position. If it is False, then that position
            cannot contain a block, or a fixed block exists there already.
    """
    def __init__(self, grid):
        self.grid = grid
        x1 = []
        for i in range(len(grid)):
            col_id = grid[i]
            x2 = []
            for j in range(len(col_id)):
                if col_id[j] == "o":
                    x2.append(True)
                else:
                    x2.append(False)
            x1.append(x2)
        self.grid_param = x1

    def __str__(self):
        s1 = "grid = " + str(self.grid)
        s2 = "grid_param = " + str(self.grid_param)
        # print type(self.grid_param[0][0])
        return '\n'.join([s1, s2])

    def place_block(self, Block, position):
        """ Place a block at a given position """
        self.grid[position[0]][position[1]] = Block.block_type
        return self.grid

    def laser(self):
        """ Specify a laser and the direction it is pointing in """
        # Laser can be represented by a system of lines/linear equations
        pass

    def point(self):
        """ Define point where the laser has to intersect """
        pass

    def refresh(self):
        """ Redraw the board once a block has been moved """
        pass


class Block(object):
    """
    Make an object to represent each individual block

    Use two types of booleans to describe the properties of the block:
    transmit = True or False
    reflect = True or False

    For no block, transmit = True, reflect = False
    Fora reflect block, transmit = False, reflect = True
    For an opaque block, transmit = False, reflect = False
    For a refract block, transmit = True, reflect = True
    """
    def __init__(self, block_type):
        """ Create new block """
        self.block_type = block_type
        if block_type == "A":
            self.transmit = False
            self.reflect = True
        elif block_type == "B":
            self.transmit = False
            self.reflect = False
        elif block_type == "C":
            self.transmit = True
            self.reflect = True
        else:
            self.transmit = True
            self.reflect = False

    def __str__(self):
        if self.block_type == "A":
            s1 = "Block Type = Reflect Block"
        elif self.block_type == "B":
            s1 = "Block Type = Opaque Block"
        elif self.block_type == "C":
            s1 = "Block Type = Reflect Block"
        else:
            return "Invalid block type"
        s2 = "Transmit = " + str(self.transmit)
        s3 = "Reflect = " + str(self.reflect)
        return '\n'.join([s1, s2, s3])


class Laser(object):
    """
    Make an object to represent each laser

    The indices of the laser can tell us if the laser is hitting a vertical
    position or a horizontal position
    """
    def __init__(self, laser):
        """ Create new board """
        self.position = (laser[0], laser[1])
        self.direction = (laser[2], laser[3])

    def __str__(self):
        s1 = "Position = " + str(self.position)
        s2 = "Direction = " + str(self.direction)
        return '\n'.join([s1, s2])


class Point(object):
    """
    Make an object to represent the intersection point
    """
    def __init__(self, point):
        """ Create new board """
        self.point = point

    def __str__(self):
        return str(self.point)


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


def main():
    # Input file name
    fptr = "mad_1.bff"
    # Read and parse through board file
    g, rflb, ob, rfrb, l, p = read_bff(fptr)
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


if __name__ == "__main__":
    main()
