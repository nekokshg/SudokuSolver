'''Program that takes a 9x9 sudoku puzzle and solves it recursively using backtracking'''

testList = [[8,-1,-1,9,3,-1,-1,-1,2],
            [-1,-1,9,-1,-1,-1,-1,4,-1],
            [7,-1,2,1,-1,-1,9,6,-1],

            [2,-1,-1,-1,-1,-1,-1,9,-1],
            [-1,6,-1,-1,-1,-1,-1,7,-1],
            [-1,7,-1,-1,-1,6,-1,-1,5],

            [-1,2,7,-1,-1,8,4,-1,6],
            [-1,3,-1,-1,-1,-1,5,-1,-1],
            [5,-1,-1,-1,6,2,-1,-1,8]]

def getBox(testlist, row, col):
    '''Function to return array based on 3x3 square that contains a specific row and column

    >>> test = [[8,-1,-1,9,3,-1,-1,-1,2],[-1,-1,9,-1,-1,-1,-1,4,-1],[7,-1,2,1,-1,-1,9,6,-1]]
    >>> row = 0
    >>> col = 4
    >>> result = getBox(test, row, col)
    >>> result
    [9, 3, -1, -1, -1, -1, 1, -1, -1]
        
    '''
    square = []
    startRow = row //3 * 3
    startCol = col //3 * 3

    for r in range(startRow, startRow+3):
        for c in range(startCol, startCol+3):
            square.append(testlist[r][c])
    
    return square

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
    square = getBox(puzzle, row,col)
    if guess in square:
        return False

    return True


def isEmpty(puzzle):
    '''Function to check if space is empty'''

    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row,col
    
    return None, None

        
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
            puzzle[row][col] = guess #test guess
            if solveSudoku(puzzle): #recursively call funciton
                return True
            
        puzzle[row][col] = -1 # reset guess
    
    return False
