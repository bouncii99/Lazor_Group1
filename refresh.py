"""
Function for calculating laser points given a certain grid
"""
import lazor

def check_position(x, xmax, y, ymax):
    return x >= 0 and x <= xmax and y >= 0 and y <= ymax


def next_position(x, y, vx, vy):
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

def reflect():
    # At the point where the laser hits the block:
    # If x is even, flip the sign of y
    # If x is odd, flip the sign of x
    # Create new laser object 
    pass

def calculate_laser(grid, laser, transmit, reflect):
    laser_points = []
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
                    print("Reflect block here")
                elif not does_transmit and not does_reflect:
                    print("Opaque block here")
                else:
                    print("Refract block here")
        else:
            break
    return laser_points


if __name__ == "__main__":
    pass