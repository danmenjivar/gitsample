'''
Intro to AI: Assignment # 6
Sudoku CSP
A Submission by Daniel Quintana Menjivar
Worked alongside: Kyle Guieb
'''
from constraint import *
ROWS = 'abcdefghi' # defining a bunch of constants to access the constraints
COLS = '123456789'
DIGITS = range(1,10) 
VARS = [row + col for row in ROWS for col in COLS]
ROWGROUPS = [[row + col for col in COLS] for row in ROWS]
COLGROUPS = [[row + col for row in ROWS] for col in COLS]
SQUAREGROUPS = [
    [ROWS[3 * rowgroup + k] + COLS[3 * colgroup + j]
     for j in range(3) for k in range(3)]
    for colgroup in range(3) for rowgroup in range(3)
]

def fetch_file(): # reads a file with a sudoku puzzle
    file_name = input('Enter a filename containing a Sudoku puzzle > ') + '.txt'
    file = open(file_name, 'r')
    game_board = []
    line = file.readline()
    while line:
        game_board.extend([int(x[0]) for x in line.split()])
        line = file.readline()
    game_board = tuple(game_board)
    print("The original puzzle is: ")
    print_tuple_board(game_board)
    return game_board

def solve_puzzle(game_board): # solves puzzle using CSP
    problem = Problem()
    for var, hint in zip(VARS, game_board):
        problem.addVariables([var], [hint] if hint in DIGITS else DIGITS)
    for vargroups in [ROWGROUPS, COLGROUPS, SQUAREGROUPS]:
        for vargroup in vargroups:
            problem.addConstraint(AllDifferentConstraint(), vargroup)
    return problem.getSolution()

def print_beautifully(var_to_value): # prints the solved puzzle nicely
    print('The solved puzzle is: ')
    board = ''
    for i, row in enumerate('abcdefghi'):
        for j, col in enumerate('123456789'):
            board += str(var_to_value[row+col])
            if j % 3 == 2:
                board += ' '
        board += '\n'
        if i % 3 == 2:
            board += '\n'
    print(board)

def print_tuple_board(game_board): # prints the initial puzzle nicely
    board = ''
    for i in range(len(game_board)):
        board += str(game_board[i])
        if ( (i + 1) % 3 == 0):
            board += ' '
        if ( (i + 1) % 9 == 0):
            board += '\n'
        if ((i + 1) % 27 == 0):
            board += '\n'
    print(board)

puzzle = fetch_file()
print_beautifully(solve_puzzle(puzzle))

