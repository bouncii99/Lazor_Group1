"""
This is the main Python script that solves Lazor puzzles.
"""
from lazor import Board
from read import read_bff
from re import sub
from textwrap import wrap


def try_solution(board):
    """
    This function generates a possible solution by placing available blocks on
    the board and refreshing the paths where the lasers travel. The function
    takes in a lazor.Board object and will update the appropriate attributes
    of the object accordingly.
    """
    board_gen, _ = Board.generate_board(board)
    Board.refresh_lasers(board_gen)


def solve(filename):
    """
    This function solves the Lazor puzzle.

    **Parameters**

        filename: *str*
            The name of the file to be solved.

    **Returns**

        solution: *list, str*
            The solution for the board. Each list in the solution corresponds
            to a row of the grid and each string element in the row
            corresponds to the appropriate location where a block can be
            placed.
    """
    # Read and parse through board file
    g, rflb, ob, rfrb, L, p = read_bff(filename)
    # Initialize board class
    board = Board(g, L, p, rflb, ob, rfrb)
    # Try random solutions using a while loop
    while True:
        try_solution(board)
        # Check if the generated board solves the puzzle
        if Board.check_solution(board):
            # Save the solution and exit the while loop
            solution = str(board.grid)
            break
        else:
            # Reinitialize the original board object
            del board
            g, rflb, ob, rfrb, L, p = read_bff(filename)
            board = Board(g, L, p, rflb, ob, rfrb)
    return solution


def board_display(filename, solution):
    """
    This function creates a text file with the solution to the desired Lazor
    puzzle.

    **Parameters**

        filename: *str*
            Name of the .bff file
        solution: *list, str*
            The solution to the puzzle in the .bff file.

    **Returns**

        None
    """
    # Retrive the name of the puzzle without the file extension
    board_name, _ = filename.split(".")
    # Open the new text file to output the solution to
    sol_file = open(board_name + "_solution.txt", "w")
    # Print solution title
    sol_file.write("Solution for " + board_name + ":\n")
    # Concatenate individual characters in the same row into one string
    cleanstring = sub('\W+', "", solution)
    cleanstring_grid = wrap(cleanstring, int(len(cleanstring) ** 0.5))
    # For each row, join the characters with spaces
    new_strings = []
    for i, j in enumerate(cleanstring_grid):
        new_strings.append(" ".join(j))
    # Write each line to the output file
    for i in new_strings:
        sol_file.write("%s\n" % i)


if __name__ == "__main__":
    # Test cases
    files = ["dark_1.bff", "mad_1.bff", "mad_4.bff",
             "mad_7.bff", "numbered_6.bff", "showstopper_4.bff",
             "tiny_5.bff", "yarn_5.bff"]
    for file in files:
        output = solve(file)
        board_display(file, output)
