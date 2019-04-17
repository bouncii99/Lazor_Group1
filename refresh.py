"""
This Python script contains functions that are used for calculating the points
in the path of a laser given a certain board to solve.
"""


def check_position(x, xmax, y, ymax):
    """
    Checks the position of a point on the grid where the laser can travel.
    Will return True or False depending on if the point is within the
    boundaries of the grid.

    **Parameters**

        x: *int*
            The x-coordinate of the current point of interest.
        xmax: *int*
            The maximum value of the x-axis (rightmost side of the grid).
        y: *int*
            The y-coordinate of the current point of interest.
        ymax: *int*
            The maximum value of the y-axis (bottom side of the grid).
    """
    return x >= 0 and x <= xmax and y >= 0 and y <= ymax


def next_position(x, y, vx, vy):
    """
    Calculates the next position that the laser will cross through based on
    the direction of the laser. Will return the new coordinates as integers.

    **Parameters**

        x: *int*
    """
    return x + vx, y + vy


def calc_center(p1, p2):
    '''
    Given the edges p1 and p2, this function will calculate the center of the
    block on which they lie.
    Will return the new coordinates as a tuple.

    **Parameters**
        p1: *list*
            The x and y coordinates of an edge point.
        p2: *list*
            The x and y coordinates of an edge point.
        x: *int*
            x coordinate of p1.
        y: *int*
            y coordinate of p1.
        nx: *int*
            x coordinate of p2.
        ny: *int*
            y coordinate of p2.
    '''
    x = p1[0]
    y = p1[1]
    nx = p2[0]
    ny = p2[1]
    if x % 2 != 0:
        return (x, ny)
    else:
        return (nx, y)


def map_to_block_grid(pos):
    '''
    Maps between the block grid and laser grid.
    '''
    nx = (pos[0] - 1) / 2
    ny = (pos[1] - 1) / 2
    return (nx, ny)


def reflect_laser(x, y, vx, vy):
    '''
    Calculates how the laser has to be reflected based on where it encounters
    a block. If the x coordinate is even, the polarity of y direction vector
    is flipped and if odd, the polarity x direction vector is flipped.
    Once done, the new position is calculated.

    **Parameters**

    x: *int*
        The x coordinate of the block.
    y: *int*
        The y coordinate of the block.
    nx: *int*
        The direction vector of x.
    ny: *int*
        The direction vector of y.
    '''
    if x % 2 != 0:
        vy = -1 * vy
    else:
        vx = -1 * vx
    nx, ny = next_position(x, y, vx, vy)
    return nx, ny, vx, vy


def calculate_laser(grid, laser, transmit, reflect):
    '''
    Checks whether the current position is on valid or not. Then goes on to
    calulate all possible points from there by considering which block(s)
    is(are) around it (none, A, B, C).
    It returns a list of points.

    **Parameters**

    grid: *list*
        This is a list of lists which contain the setup of the board.
    laser: *list*
        Contains the coordinate of the laser and the diretion of travel.
    transmit: *list*
        A parameter that determines whether a type of block is allowed to
        transmit the laser or not.
    reflect: *list*
        A paramter that determines wheter a type of block is allowed to
        reflect the laser or not.
    '''
    laser_points, lp = [], []
    cx = laser[0]
    cy = laser[1]
    vx = laser[2]
    vy = laser[3]
    xmax = 2 * (len(grid[0]) - 1) + 2
    ymax = 2 * (len(grid) - 1) + 2
    while True:
        # Check if the current point is in the grid
        if check_position(cx, xmax, cy, ymax):
            pos = (cx, cy)
            laser_points.append(pos)
            # Calculate the possible next point
            nx, ny = next_position(cx, cy, vx, vy)
            if check_position(nx, xmax, ny, ymax):
                # Define the center of the block we are adjacent to
                center = calc_center((cx, cy), (nx, ny))
                block_position = map_to_block_grid(center)
                # Determine if the block transmits and/or reflects the laser
                does_transmit = transmit[block_position[1]][block_position[0]]
                does_reflect = reflect[block_position[1]][block_position[0]]
                # 4 possible cases
                if does_transmit and not does_reflect:
                    # No block
                    cx = nx
                    cy = ny
                elif not does_transmit and does_reflect:
                    # Reflect block
                    cx, cy, vx, vy = reflect_laser(cx, cy, vx, vy)
                elif not does_transmit and not does_reflect:
                    # Opaque block
                    break
                else:
                    # Refract block
                    nx2, ny2, vx2, vy2 = reflect_laser(cx, cy, vx, vy)
                    center_calc = calc_center((cx, cy), (nx2, ny2))
                    block_pos = map_to_block_grid(center_calc)
                    transmit_rfrb = transmit[block_pos[1]][block_pos[0]]
                    if transmit_rfrb:
                        lp = calculate_laser(grid, [nx2, ny2, vx2, vy2],
                                             transmit, reflect)
                    cx = nx
                    cy = ny
            else:
                break
        else:
            break
    for point in lp:
        laser_points.append(point)
    return laser_points


def main():
    grid = [['x', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'x']]
    laser = [3, 0, -1, 1]
    transmit_array = [[True, True, True], [True, True, True],
                      [True, True, True]]
    reflect_array = [[False, False, False], [False, False, False],
                     [False, False, False]]
    lp = calculate_laser(grid, laser, transmit_array, reflect_array)
    print(lp)


if __name__ == '__main__':
    main()
