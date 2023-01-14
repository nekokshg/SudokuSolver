'''Program that takes a 9x9 sudoku puzzle and solves it recursively using backtracking'''

testList = [[8,-1,-1,9,3,-1,-1,-1,2],
            [-1,-1,9,-1,-1,-1,-1,4,-1],
            [7,-1,2,1,-1,-1,-1,9,6,-1],
            [2,-1,-1,-1,-1,-1,-1,9,-1],
            [-1,6,-1,-1,-1,-1,-1,7,-1],
            [-1,6,-1,-1,-1,6,-1,-1,5],
            [-1,2,7,-1,-1,8,4,-1,6],
            [-1,3,-1,-1,-1,-1,5,-1,-1],
            [5,-1,-1,-1,6,2,-1,-1,8]]


def isValid(puzzle, guess, row, col):
    '''Function to put a valid number in empty space'''
    
    #check if guess in row
    rowCheck = puzzle[row]
    if guess in rowCheck:
        return False

    #check if guess in column
    for r in range (9):
        if guess == puzzle[r][col]:
            return False

    #check if guess in 3x3 square
    
    return True


def isEmpty(puzzle):
    '''Function to check if space is empty'''

    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row,col
    
    return None, None

def printPuzzle(puzzle):
    '''Function to print entire puzzle'''

    for row in range(9):
        for col in range(9):
            print(puzzle[row][col])
        
def solveSudoku(puzzle):
    '''Function to solve sudoku puzzle'''

    #Find an empty space in the puzzle
    row,col = isEmpty(puzzle)

    #If there is no empty space the puzzle is solved
    if row == None:
        return True

    #Fill empty space with valid guess number
    for guess in range(1,10):
        if isValid(puzzle, guess, row, col):
            puzzle[row][col] = guess
