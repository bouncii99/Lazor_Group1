"""
This file contains the class definitions for the blocks, lasers, intersection
points, and the board itself.
"""
import Read
import numpy as np


class Block(object):
    """
    This class represents each individual block that can be placed onto the
    board. We use two boolean variables to describe the properties of the each
    block:
        transmit - whether or not the block allows the laser to continue to
                   travel in the same direction.
        reflect - whether or not the block reflects the laser in the
                  appropriate perpendicular direction.
    There are four cases corresponding to the three different types of blocks
    and when a spot has no block:
        For a spot with no block, transmit = True and reflect = False.
        For a reflect block, transmit = False and reflect = True.
        For an opaque block, transmit = False and reflect = False.
        For a refract block, transmit = True and reflect = True.

    **Parameters**

        block_type: *str*
            The type of the block. 'A' corresponds to the reflect block, 'B'
            corresponds to the opaque block, and 'C' corresponds to the
            refract block.
    """
    def __init__(self, block_type):
        # Define the type of block
        self.block_type = block_type
        # Use conditionals to appropriately set the boolean properties of the
        # block
        if block_type == 'A':
            self.transmit = False
            self.reflect = True
        elif block_type == 'B':
            self.transmit = False
            self.reflect = False
        elif block_type == 'C':
            self.transmit = True
            self.reflect = True
        else:
            self.transmit = True
            self.reflect = False

    def __repr__(self):
        s1 = "block type = " + str(self.block_type)
        s2 = "transmit = " + str(self.transmit)
        s3 = "reflect = " + str(self.reflect)
        return '\n'.join([s1, s2, s3])

    def __str__(self):
        if self.block_type == 'A':
            return "This block is a reflect block."
        elif self.block_type == 'B':
            return "This block is an opaque block."
        elif self.block_type == "C":
            return "This block is a reflect block."
        else:
            return "This is not a block."


class Laser(object):
    """
    This class represents a laser on the board.

    **Parameters**

        laser: *list, int*
            A list of integers representing the laser. The first two integers
            correspond to the position of the laser and the last two integers
            correspond to the direction it is pointing in.
    """
    def __init__(self, laser):
        self.position = (laser[0], laser[1])
        self.direction = (laser[2], laser[3])

    def __repr__(self):
        s1 = "position = " + str(self.position)
        s2 = "direction = " + str(self.direction)
        return '\n'.join([s1, s2])

    def __str__(self):
        unit_vectors = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        d = ["southeast", "northeast", "northwest", "southwest"]
        i = unit_vectors.index(self.direction)
        s1 = "This laser starts at position " + str(self.position)
        s2 = "and is pointing " + d[i] + "."
        return ' '.join([s1, s2])


class Point(object):
    """
    This class represents a point on the board where the laser must intersect
    in order to solve the board.

    **Parameters**

        point: *list, int*
            A list of integers representing the coordinates of the point on
            the grid.
    """
    def __init__(self, point):
        self.point = point

    def __repr__(self):
        return str(self.point)

    def __str__(self):
        return "The laser must intersect at " + str(self.point)


class Board(object):
    """
    The Board class represents the entire Lazors game board, including the
    lasers, blocks, and desired intersection points.

    **Parameters**

        grid: *list, str*
            The list of characters that represents all of the available spots
            on the board. Each list inside the list represents a row of the
            board.
        valid_positions: *list, boolean*
            A list of True and False parameters corresponding to all of the
            positions on the board. If valid_positions is True, then a block
            can be placed in that position. If it is False, then that position
            cannot contain a block, or a fixed block exists there already.
    """
    def __init__(self, grid):
        # Define grid
        self.grid = grid
        # Generate list of valid positions
        pos_temp = []
        for i in range(len(grid)):
            col_id = grid[i]
            bool_temp = []
            for j in range(len(col_id)):
                if col_id[j] == "o":
                    bool_temp.append(True)
                else:
                    bool_temp.append(False)
            pos_temp.append(bool_temp)
        self.valid_positions = pos_temp

    def __str__(self):
        s1 = "grid = " + str(self.grid)
        s2 = "valid positions = " + str(self.valid_positions)
        return '\n'.join([s1, s2])

    def pos_check(self, x, y):
        """ Check if a grid position is valid """
        x_max = len(self.grid)
        y_max = len(self.grid[0])
        return x >= 0 and x < x_max and y >= 0 and y < y_max

    def place_block(self, Block, pos):
        """ Place a block at a given position """
        x = pos[0]
        y = pos[1]
        # Check if the position is valid
        if Board.pos_check(self, x, y) and self.valid_positions[x][y]:
            self.grid[x][y] = Block.block_type
            self.valid_positions[x][y] = False
            return self.grid, self.valid_positions
        else:
            return "Invalid position"

    def random_placement(self):
        """ Calls the place_block function to randomly place blocks """
        x_upper = 
        x = np.random.choice([range(len(self.grid[0]))], True)
        y = np.random.choice([range(len(self.grid[0]))], True)
        # return self.x, self.y
        print (type(x), type(y))

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


def main():
    # Input file name
    fptr = "showstopper_4.bff"
    # Read and parse through board file
    g, rflb, ob, rfrb, l, p = Read.read_bff(fptr)
    test = Point(p[0])
    print(repr(test))
    grid = Board(g)
    print grid
    Board.random_placement(grid)


if __name__ == "__main__":
    main()
