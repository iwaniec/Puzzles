import numpy as np

# Puzzle initialization (0 means unknown value)
puzzle =  np.array([[1, 2, 4, 3, 9, 6, 5, 0, 0],
                    [7, 0, 0, 0, 0, 0, 3, 9, 2],
                    [0, 9, 0, 0, 0, 0, 0, 4, 0],
                    [0, 0, 0, 4, 3, 9, 2, 0, 0],
                    [0, 7, 0, 0, 0, 0, 0, 5, 0],
                    [0, 0, 2, 6, 5, 7, 0, 0, 0],
                    [0, 4, 0, 0, 0, 0, 0, 6, 0],
                    [2, 6, 7, 0, 0, 0, 0, 0, 9],
                    [0, 0, 8, 1, 6, 3, 7, 2, 4]])

# puzzle =  np.array([[0, 1, 6, 7, 0, 5, 3, 0, 0],
#                     [4, 0, 0, 0, 6, 0, 0, 0, 0],
#                     [2, 0, 0, 0, 0, 0, 0, 0, 1],
#                     [6, 0, 0, 0, 0, 0, 0, 0, 0],
#                     [0, 0, 0, 0, 0, 3, 0, 8, 0],
#                     [0, 9, 7, 0, 5, 0, 0, 0, 4],
#                     [0, 2, 0, 0, 0, 0, 0, 0, 0],
#                     [0, 0, 0, 9, 0, 0, 4, 0, 0],
#                     [0, 5, 1, 0, 7, 0, 0, 0, 9]])

# Is this value a possibilty?
solver = np.full((9, 9, 9), True)

def simple_elimination():
    for row in range(9):
        for col in range(9):

            # get the value of the puzzle at a position
            value = puzzle[row, col]

            # if the value is known ...
            if value > 0:

                # Remove value as possibilty from row
                solver[:, col, value-1] = False
                # Remove value as possibilty from column
                solver[row, :, value-1] = False
                # Remove value as possibilty from square
                rows = np.arange( 3*(row//3), (3*(row//3)+3) )
                cols = np.arange( 3*(col//3), (3*(col//3)+3) )
                solver[rows, cols, value-1] = False


def update_puzzle():
    for row in range(9):
        for col in range(9):
            if puzzle[row, col] == 0 and sum(solver[row, col, :]) == 1:
                puzzle[row, col] = sum(range(9)*solver[row, col, :])+1

i= 0
while True:
    i += 1

    prev_puzzle = np.copy(puzzle)
    simple_elimination()
    update_puzzle()

    print('Iteration:', i)
    print(puzzle)

    # If a further step was not possible
    if (puzzle == prev_puzzle).all():
        print('Cannot Solve Further :(')
        break

    # If the puzzle is complete
    if np.all(puzzle):
        print('Puzzle Completed')
        break
