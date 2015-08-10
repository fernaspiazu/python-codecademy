from random import randint

__author__ = 'fumandito'

board = []

for i in range(5):
    board.append(["O"] * 5)


def print_board(_board):
    for row in _board:
        print " ".join(row)
    print


def random_row(_board):
    return randint(0, len(_board) - 1)


def random_col(_board):
    return randint(0, len(_board) - 1)


for turn in range(4):
    ship_row = random_row(board)
    ship_col = random_col(board)
    print ship_row
    print ship_col

    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already."
        else:
            if turn == 3:
                print "Game Over"
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        print "Turn %s" % (turn + 1)
        print_board(board)
