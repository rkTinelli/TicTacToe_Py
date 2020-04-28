import random as rnd

# Empty board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Display the board for the player in the console
def showBoard(board):
    for i in range(3):
        for j in range(3):
            if j != 2:
                print(" " + board[i][j] + " |", end='')
            else:
                print(" " + board[i][j] + " ", end='\n')
        if i != 2:
            print("___________")

# Check if the position in the board is empty
def checkIfEmpty(board, pos):
    if board[pos[0]][pos[1]] != " ":
        return False
    return True

# Simulate the computer turn, verifies if empty, if so, populates it with "X"
# # Using recursive method will make a loop until a valid position is provided
def computerTurn(board):
    pc_X = rnd.randrange(0, 3)
    pc_Y = rnd.randrange(0, 3)
    if checkIfEmpty(board, (pc_X, pc_Y)):
        board[pc_X][pc_Y] = "O"
        return True
    else:
        computerTurn(board)

# Get the player input, verifies if empty, if so, populates it with "X"
# Using recursive method will make a loop until a valid position is provided
def playerTurn(board):
    play_response = (input("Please give the X,Y coordinates of your play: "))
    play_pos = list(map(int, play_response.split(",")))
    if checkIfEmpty(board, (play_pos[0], play_pos[1])):
        board[play_pos[0]][play_pos[1]] = "X"
        return True
    else:
        print("Positions occupied, please try again")
        playerTurn(board)

# Check if the game resulted in a tie, if there is no spaces available to play
def checkTie(board):
    # Check all the spaces in the board to
    # find an empty space, if found, return False, else return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
            return True


def checkWin(Board,symbol):
    # Check lines
    for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == symbol:
                return True

    # Check column
    for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] == symbol:
                return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    return False


computerTurn(board)
showBoard(board)