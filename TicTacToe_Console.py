import random as rnd

# Empty board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def showBoard(board):
    for i in range(3):
        for j in range(3):
            if j != 2:
                print(" " + board[i][j] + " |", end='')
            else:
                print(" " + board[i][j] + " ", end='\n')
        if i != 2:
            print("___________")


def checkIfEmpty(board, pos):
    if board[pos[0]][pos[1]] != " ":
        print("Positions occupied, please try again")
        return False
    return True


def computerTurn(board):
    pc_X = rnd.randrange(0, 3)
    pc_Y = rnd.randrange(0, 3)
    if checkIfEmpty(board, (pc_X, pc_Y)):
        board[pc_X][pc_Y] = "O"
        return True
    else:
        computerTurn(board)


def playerTurn(board):
    play_response = (input("Please give the X,Y coordinates of your play: "))
    play_pos = list(map(int, play_response.split(",")))
    if checkIfEmpty(board, (play_pos[0], play_pos[1])):
        board[play_pos[0]][play_pos[1]] = "X"
        return True
    else:
        playerTurn(board)


def checkDraw(board):
    # Check all the spaces in the board to
    # find an empty space, if found, return False, else return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
            return True


playerTurn(board)
computerTurn(board)
showBoard(board)
