import random

def find_next_empty(puzzle):
    #This function is used to return the indies of emppty spaces present.
    #sudoko is built using the 9x9 matrix. Which is built using list of list
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==-1:
                return r,c
    
    return None,None

def is_valid(puzzle,guess,row,col):
    #figues out wether the guess is valid or not
    #returns true if it is valid else false
    
    #first checking row values
    row_vals=puzzle[row]
    if guess in row_vals:
        return False

    #Build column values and checking
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    #step3:checking the guessed value is present in the submatrix
    row_start = (row//3)*3
    col_start = (col//3)*3
    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if guess == puzzle[r][c]:
                return False

    return True

def solve_sudoko(puzzle):
    #solve the puzzle using back tracking
    #Our puzzle is list of list where inner list is the row in the puzzle

    #step1: Choose some where on the puzzle to guess
    row,col=find_next_empty(puzzle)

    #returns true if there is no space left
    if row==None:
        return True

    #step2: guess a number between 1 to 9
    for guess in range(1,10):
        #check if this is the valid guess or not
        if is_valid(puzzle,guess,row,col):
            #place the guessed value in the place
            puzzle[row][col]=guess

            if solve_sudoko(puzzle): #recurssive to check the every value
                return True

        #replace the value by -1 if there is no match
        puzzle[row][col]=-1

    #return false if the puzzle can't be solved
    return False

if __name__ == '__main__':
    # example_board = list()
    # for r in range(9):
    #     row = []
    #     for c in range(9):
    #         row.append(random.randint(-1,9))

    #     example_board.append(row)

    example_board = [[3,9,-1,-1,5,-1,-1,-1,-1],[-1,-1,-1,2,-1,-1,-1,-1,5],[-1,-1,-1,7,1,9,-1,8,-1],
                     [-1,5,-1,-1,6,8,-1,-1,-1],[2,-1,6,-1,-1,3,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,4],
                     [5,-1,-1,-1,-1,-1,-1,-1,-1],[6,7,-1,1,-1,5,-1,4,-1],[1,-1,9,-1,-1,-1,2,-1,-1]]
    print(example_board)
    #print(solve_sudoko(example_board))
    print(example_board)
    # print(example_board)
    # print(solve_sudoko(example_board))
    # print(example_board)

