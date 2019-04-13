"""
This file contains the class definitions for the blocks, lasers, intersection
points, and the board itself.
"""
import random
import read


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
        # Use conditionals to appropriately set the Boolean properties of the
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
        xbound: *int*
            The rightmost boundary of the grid. This value is used to specify
            the possible domain of points that the laser intersects.
        ybound: *int*
            The bottom boundary of the grid. This value is used to specify
            the possible range of points that the laser intersects.
    """
    def __init__(self, laser, xbound, ybound):
        # Define position and direction as given
        x = laser[0]
        y = laser[1]
        vx = laser[2]
        vy = laser[3]
        self.position = (x, y)
        self.direction = (vx, vy)
        # Define the laser as a linear equation: y = mx + c
        x2 = x + vx
        y2 = y + vy
        self.m = (y2 - y) / (x2 - x)
        self.c = y - (self.m * x)
        # Represent the line as all the points that make up the line that are
        # within the grid
        laser_points = []
        xmax = 2 * xbound + 2
        ymax = 2 * ybound + 2
        for i in range(xmax):
            j = self.m * i + self.c
            if j >= 0 and j <= ymax:
                coordinates = (i, j)
                laser_points.append(coordinates)
        self.laser_points = laser_points
        
    def __repr__(self):
        s1 = "position = " + str(self.position)
        s2 = "direction = " + str(self.direction)
        s3 = "slope = " + str(self.m)
        s4 = "y-int = " + str(self.c)
        s5 = "laser points = " + str(self.laser_points)
        return '\n'.join([s1, s2, s3, s4, s5])

    def __str__(self):
        unit_vectors = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        d = ["southeast", "northeast", "northwest", "southwest"]
        i = unit_vectors.index(self.direction)
        s1 = "This laser starts at position " + str(self.position)
        s2 = "and is pointing " + d[i] + "."
        s3 = "This is represented by the line y = " + m + "x + " + c
        return ' '.join([s1, s2, s3])


# class Point(object):
#     """
#     This class represents a point on the board where the laser must intersect
#     in order to solve the board.

#     **Parameters**

#         point: *list, int*
#             A list of integers representing the coordinates of the point on
#             the grid.
#     """
#     def __init__(self, point):
#           point = p
#         self.point = point

#     def __repr__(self):
#         return str(self.point)

#     def __str__(self):
#         return "The laser must intersect at " + str(self.point)


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
        xmax: *int*
            The maximum range of the grid in the x-direction.
        ymax: *int*
            The maximum range of the grid in the y-direction.
    """
    def __init__(self, grid, lasers):
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
        # Define dimensions
        self.xmax = len(self.grid[0]) - 1
        self.ymax = len(self.grid) - 1
        # Initialize lasers
        l = []
        for i in lasers:
            l.append(Laser(i, self.xmax, self.ymax))
        self.lasers = l
    
    def __repr__(self):
        s1 = "grid: " + str(self.grid)
        s2 = "valid positions: " + str(self.valid_positions)
        s3 = "lasers: " + str(self.lasers)
        return '\n'.join([s1, s2, s3])
      
    def __str__(self):
        s1 = "The current board is " + str(self.grid)
        s2 = "The valid positions for the board are " + str(self.valid_positions)
        return '\n'.join([s1, s2])
    
    def pos_check(self, x, y):
        """ Check if a grid position is valid """
        return x >= 0 and x < self.xmax and y >= 0 and y < self.ymax

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
            print("Invalid position")

    def random_placement(self, Block):
        """ Calls the place_block function to randomly place blocks """
        x = random.randint(range(self.xmax))
        y = random.randint(range(self.ymax))
        pos = (x, y)
        Board.place_block(Block, pos)
        # return self.pos

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
    g, rflb, ob, rfrb, l, p = read.read_bff(fptr)
    test_board = Board(g, l)


if __name__ == "__main__":
    main()
