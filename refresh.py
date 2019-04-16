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
    x = p1[0]
    y = p1[1]
    nx = p2[0]
    ny = p2[1]
    if x % 2 != 0:
        return (x, ny)
    else:
        return (nx, y)


def map_to_block_grid(pos):
    nx = (pos[0] - 1) / 2
    ny = (pos[1] - 1) / 2
    return (nx, ny)


def reflect_laser(x, y, vx, vy):
    # If x is even, flip the sign of vy
    if x % 2 != 0:
        vy = -1 * vy
    # If x is odd, flip the sign of vx
    else:
        vx = -1 * vx
    # Calculate new position
    nx, ny = next_position(x, y, vx, vy)
    return nx, ny, vx, vy


def calculate_laser(grid, laser, transmit, reflect):
    laser_points, lp = [], []
    cx = laser[0]
    cy = laser[1]
    vx = laser[2]
    vy = laser[3]
    initial_direction = (vx, vy)
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
                    lp = calculate_laser(grid, [nx2, ny2, vx2, vy2], transmit, reflect)
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
    transmit_array = [[True, True, True], [True, True, True], [True, True, True]]
    reflect_array = [[False, False, False], [False, False, False], [False, False, False]]
    lp = calculate_laser(grid, laser, transmit_array, reflect_array)
    print(lp)


if __name__ == '__main__':
    main()
