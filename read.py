"""
This Python script contains a function that reads in a BFF file as specified
by the user.
"""
from re import findall


def read_bff(filename):
    """
    Reads and parses through the .bff file.

    **Parameters**

        filename: *str*
            The name of the .bff file to be read in.

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
    # represents the grid or not
    in_grid = False
    # Open the file and read through each line
    raw_lines = open(filename, 'r')
    for index, line in enumerate(raw_lines):
        # Parse through the grid portion of the file
        if "GRID STOP" in line:
            in_grid = False
        if in_grid:
            line = line.replace(" ", "")
            line = line.replace("\t", "")
            grid.append(list(line.strip("\n")))
        if "GRID START" in line:
            in_grid = True
        # Parse through the blocks
        if line[0] == 'A':
            reflect_blocks = [int(s) for s in line if s.isdigit()]
        elif line[0] == 'B':
            opaque_blocks = [int(s) for s in line if s.isdigit()]
        elif line[0] == 'C':
            refract_blocks = [int(s) for s in line if s.isdigit()]
        # Parse through the lasers and intersection points
        if line[0] == 'L':
            lasers.append([int(s) for s in findall(r'-?\d', line)])
        if line[0] == 'P':
            points.append([int(s) for s in line if s.isdigit()])
    # Convert block lists to appropriate integers
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
    # Test the read_bff function
    file = "dark_1.bff"
    g, rflb, ob, rfrb, L, p = read_bff(file)
    print("Grid:")
    for i in g:
        print(i)
    print("\nReflect blocks: " + str(rflb))
    print("Opaque blocks: " + str(ob))
    print("Refract blocks: " + str(rfrb))
    print("\nLasers:")
    for i in L:
        print(i)
    print("\nPoints that need the lasers to intersect:")
    for i in p:
        print(i)
    print len(g)


if __name__ == '__main__':
    main()
