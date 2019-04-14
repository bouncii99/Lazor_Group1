"""
This file contains the class definitions for the blocks, lasers, intersection
points, and the board itself.
"""
import random
import refresh


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
    def __init__(self, laser, grid):
        # Define position and direction as given
        x = laser[0]
        y = laser[1]
        vx = laser[2]
        vy = laser[3]
        self.position = (x, y)
        self.direction = (vx, vy)
        # Represent the line as all the points that make up the line that are
        # within the grid
        self.laser_points = refresh.calculate_laser(grid, laser)
        
    def __repr__(self):
        s1 = "position = " + str(self.position)
        s2 = "direction = " + str(self.direction)
        s3 = "laser points = " + str(self.laser_points)
        return '\n'.join([s1, s2, s3])

    def __str__(self):
        unit_vectors = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        d = ["southeast", "northeast", "northwest", "southwest"]
        i = unit_vectors.index(self.direction)
        s1 = "This laser starts at position " + str(self.position)
        s2 = "and is pointing " + d[i] + "."
        s3 = "The laser covers the following points: " + str(self.laser_points)
        return ' '.join([s1, s2, s3])


class Board(object):
    """
    The Board class represents the entire Lazors game board, including the
    lasers, blocks, and desired intersection points.

    **Parameters**

        grid: *list, str*
            The list of characters that represents all of the available spots
            on the board. Each list inside the list represents a row of the
            board.
    """
    def __init__(self, grid, lasers, points, reflect, opaque, refract):
        # Define grid
        self.grid = grid
        # Define dimensions
        self.xmax = len(self.grid[0]) - 1
        self.ymax = len(self.grid) - 1
        # Initialize lasers
        l = []
        for i in lasers:
            l.append(Laser(i, self.grid))
        self.lasers = l
        # Initialize intersection points
        p = []
        for i in points:
            p.append(i)
        self.points = p
        # Initialize blocks available for placement
        self.blocks = [reflect, opaque, refract]
        # Generate arrays of booleans for reflect and transmit
        transmit_arr, reflect_arr = [], []
        for i in range(len(grid)):
            col_id = grid[i]
            bool_temp1, bool_temp2 = [], []
            for j in range(len(col_id)):
                if col_id[j] == 'A':
                    bool_temp1.append(False)
                    bool_temp2.append(True)
                elif col_id[j] == 'B':
                    bool_temp1.append(False)
                    bool_temp2.append(False)
                elif col_id[j] == 'C':
                    bool_temp1.append(True)
                    bool_temp2.append(True)
                else:
                    bool_temp1.append(True)
                    bool_temp2.append(False)
            transmit_arr.append(bool_temp1)
            reflect_arr.append(bool_temp2)
        self.transmit = transmit_arr
        self.reflect = reflect_arr


    def __repr__(self):
        s1 = "grid: " + str(self.grid)
        s2 = "xmax = " + str(self.xmax)
        s3 = "ymax = " + str(self.ymax)
        s4 = "lasers:\n" + str(self.lasers)
        s5 = "points:\n" + str(self.points)
        s6 = "transmit: " + str(self.transmit)
        s7 = "reflect: " + str(self.reflect)
        s8 = "blocks: " + str(self.blocks)
        return '\n'.join([s1, s2, s3, s4, s5, s6, s7, s8])
      
    def __str__(self):
        s1 = str(self.grid)
        return s1
    
    def pos_check(self, x, y):
        """ Check if a grid position is valid """
        return x >= 0 and x <= self.xmax and y >= 0 and y <= self.ymax

    # def pos_check_laser(self, pos):
    #     """ Check if a grid position for the lasers is valid """
    #     x = pos[0]
    #     y = pos[1]
    #     return x >= 0 and x <= 2 * self.xmax + 2 and y >= 0 and y <= 2 * self.ymax + 2

    def place_block(self, block, pos):
        """ Place a block at a given position """
        x = pos[0]
        y = pos[1]
        # Check if the position is valid
        if Board.pos_check(self, x, y) and self.grid[y][x] == 'o':
            self.grid[y][x] = block
            return self.grid
        else:
            return -1

    def generate_board(self, blocks):
        """ Calls the place_block function to randomly place blocks """
        block_list, block_positions = [], []
        for i in range(blocks[0]):
            block_list.append('A')
        for i in range(blocks[1]):
            block_list.append('B')
        for i in range(blocks[2]):
            block_list.append('C')
        for i in block_list:
            while True:
                x = random.randint(0, self.xmax)
                y = random.randint(0, self.ymax)
                pos = (x, y)
                temp = Board.place_block(self, i, pos)
                if temp != -1:
                    block_positions.append(pos)
                    break
        return block_positions

    # def generate_board(self):
    #     """
    #     1. Randomly place all blocks
    #     2. Determine position of all blocks
    #     3. For each block, check if it intersects with a block.
    #     4. Determine new laser path.
    #     5. Check if all points are satisfied
    #     6. Repeat and discount the old position from the new possible combinations
    #     If possible, bias refract block to be near the centre of the grid
    #     """
    #     v = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    #     for i, j in enumerate(self.blocks):
    #         # Randomly place the block on the board
    #         pos = Board.random_placement(self, j)
    #         print("Block is placed at:")
    #         print(pos)
    #         # Retrieve the position at which the block has been placed
    #         block_center = tuple([2 * i + 1 for i in pos])
    #         cx = block_center[0]
    #         cy = block_center[1]
    #         block_sides = []
    #         for k in range(len(v)):
    #             nx = cx + v[k][0]
    #             ny = cy + v[k][1]
    #             block_sides.append((nx, ny))
    #         for k in self.lasers:
    #             print("Points at which laser intersects on the board:")
    #             print(k.laser_points)
    #             matches = list(set(k.laser_points).intersection(block_sides))
    #             if len(matches) > 0:
    #                 xint = matches[0][0]
    #                 yint = matches[0][1]
    #                 laser_loc = k.laser_points.index((xint, yint))
    #                 print("There is a match at (%d, %d)" % (xint, yint))
    #                 print("Index at %d" % laser_loc)
    #                 if j.block_type == 'A':
    #                     if xint % 2 == 0:
    #                         while pos_check_laser(self, k.laser_points[-1]):
    #                             vx = -1 * k.direction[0]
    #                             vy = k.direction[1]
    #                             xint += vx
    #                             yint += vy
    #                             k.laser_points.append((xint, yint))     
    #                 elif j.block_type == 'B':
    #                     Laser.remove_points(k, laser_loc)
    #                     print(k.laser_points)
    #                 elif j.block_type == 'C':
    #                     if xint % 2 == 0:
    #                         while pos_check_laser(self, k.laser_points[-1]):
    #                             vx = -1 * k.direction[0]
    #                             vy = k.direction[1]
    #                             xint += vx
    #                             yint += vy
    #                             k.laser_points.append((xint, yint))
    #             else:
    #                 print("No matches, check the next laser.")

                                
            