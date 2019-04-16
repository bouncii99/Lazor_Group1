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
    def __init__(self, laser, grid, transmit, reflect):
        self.laser = laser
        # Define position and direction as given
        x = laser[0]
        y = laser[1]
        vx = laser[2]
        vy = laser[3]
        self.position = (x, y)
        self.direction = (vx, vy)
        # Represent the line as all the points that make up the line that are
        # within the grid
        self.laser_points, _ = refresh.calculate_laser(
            grid, self.laser, transmit, reflect)

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
        # Initialize lasers
        L = []
        for i in lasers:
            L.append(Laser(i, self.grid, self.transmit, self.reflect))
        self.lasers = L
        # Initialize intersection points
        p = []
        for i in points:
            p.append(i)
        self.points = p
        # Initialize blocks available for placement
        self.blocks = [reflect, opaque, refract]

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

    def place_block(self, block, pos, transmit, reflect):
        """ Place a block at a given position """
        x = pos[0]
        y = pos[1]
        # Check if the position is valid
        if Board.pos_check(self, x, y) and self.grid[y][x] == 'o':
            self.grid[y][x] = block
            if block == 'A':
                self.transmit[y][x] = False
                self.reflect[y][x] = True
            elif block == 'B':
                self.transmit[y][x] = False
                self.reflect[y][x] = False
            elif block == 'C':
                self.transmit[y][x] = True
                self.reflect[y][x] = True
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
                transmit = self.transmit[y][x]
                reflect = self.reflect[y][x]
                temp = Board.place_block(self, i, pos, transmit, reflect)
                if temp != -1:
                    block_positions.append(pos)
                    break
        return block_positions

    def refresh_lasers(self):
        new_list = []
        for i in self.lasers:
            new_list.append(i)
        lp = []
        while len(new_list) > 0:
            current_laser = new_list[0]
            x, y = current_laser.position
            vx, vy = current_laser.direction
            points, new_lasers = refresh.calculate_laser(
                self.grid, [x, y, vx, vy], self.transmit, self.reflect)
            if len(new_lasers) > 0:
                for i in new_lasers:
                    new_list.append(i)
            lp.append(points)
            new_list.pop(0)
        for i, j in enumerate(self.lasers):
            j.laser_points = lp[i]
        return self.lasers

    def check_solution(self):
        complete_list = []
        for i in self.lasers:
            for j in i.laser_points:
                complete_list.append(j)
        points = map(tuple, self.points)
        return set(points).issubset(complete_list)
