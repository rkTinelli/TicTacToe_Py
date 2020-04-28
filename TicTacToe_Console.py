# Empty board
board = [
    ["X"," "," "],
    [" "," "," "],
    [" "," "," "]
]

def showBoard(board):
    for i in range(3):
        for j in range(3):
            if j != 2:
                print(" " +board[i][j] + " |", end='')
            else:
                print(" " + board[i][j] + " ", end='\n')
        if i != 2:
            print("___________")


def checkIfEmpty(board,pos):
    if board[pos[0]][pos[1]] != " ":
        print("Positions occupied, please try again")
        return False
    return True


showBoard(board)
