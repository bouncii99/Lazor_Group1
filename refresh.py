"""
Function for calculating laser points given a certain grid
"""

def calculate_laser(grid, laser):
    laser_points = []
    x = laser[0]
    y = laser[1]
    vx = laser[2]
    vy = laser[3]
    xmax = 2 * (len(grid[0]) - 1) + 2
    ymax = 2 * (len(grid) - 1) + 2
    while True:
        pos = (x, y)
        if x >= 0 and x <= xmax and y >= 0 and y <= ymax:
            laser_points.append(pos)
        else:
            break
        x += vx
        y += vy
    return laser_points


if __name__ == "__main__":
    pass