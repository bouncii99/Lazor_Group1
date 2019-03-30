class Board:
    """
    Board class represents the Lazors game board.

    **Parameters**

        list all parameters that appear in __init__
        rows: ints
        columns: ints
    """

    def __init__(self, rows, columns):
        """ Create new board """
        self.rows = rows
        self.columns = columns

    def __repr__(self):
        """ Representation of the object for debugging """
        pass

    def __str__(self):
        """ String representation of the object """
        pass

    def add_block(self, block_type):
        """ Add a block to the board """
        pass

    def place_block(self):
        """ Place a block at a given position """
        pass

    def laser(self, x, y, vx, vy):
        """ Specify a laser and the direction it is pointing in """
        # Laser can be represented by a system of lines/linear equations
        pass

    def point(self):
        """ Define point where the laser has to intersect """
        pass

    def refresh(self):
        """ Redraw the board once a block has been moved """
        pass


def read_bff(filename):
    """ Reads through the .bff file """
    with open(filename) as fp:
        for cnt, line in enumerate(fp):
            print("Line {}: {}".format(cnt, line))


if __name__ == "__main__":
    fptr = "dark_1.bff"
    read_bff(fptr)
