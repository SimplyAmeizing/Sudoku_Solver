#program uses a recursive backtracking algorithm to solve any sudoku board


#this is the unsolved sudoku board
board = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]        
        ]



#prints board
def board_p(boa):
    for i in range(len(boa)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - -')
        
        for j in range(len(boa[0])):
            if j % 3 == 0 and j != 0:
                print('|',end='')
                
            if j == 8:
                print(boa[i][j])
            else:
                print(str(boa[i][j]) + ' ', end='')

#finds any and all parts/points on the sudoku board that read zero/unsolved
def empty_square(boa):
    for i in range(len(boa)):
        for j in range(len(boa[0])):
            if boa[i][j] == 0:
                return (i,j)
    
    return None
                


#actual solving algorithm that calls upon other functions and solved the board
def solver(boa):
    find = empty_square(boa)
    if not find:
        return True
    else:
        row, col = find
        
    for i in range(1,10):
        if valid_square(boa, i, (row, col)):
            boa[row][col] = i
            
            if solver(boa):
                 return True
            boa[row][col] = 0
            
    return False

#checks validity of certain squares
def valid_square(boa, num, pos):    
    #check if row is valid
    for i in range(len(boa[0])):
        if boa[pos[0]][i] == num and pos[1] != i:
            return False
    #checking column
    for i in range(len(boa)):
        if boa[i][pos[1]] == num and pos[0] != i:
            return False       
    #box
    xbox = pos[1] // 3
    ybox = pos[0] // 3
    for i in range(ybox * 3, ybox * 3 + 3):
        for j in range(xbox * 3, xbox * 3 + 3):
            if boa[i][j] == num and (i,j) != pos:
                return False
    
    return True

#prints the board
board_p(board)
solver(board)
print('____________________')
board_p(board)
