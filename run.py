board = [" "] * 10

def display_board(board):
    print('    |      |')
    print("", board[7], ' | ', board[8], "", ' | ', board[9])
    print('    |      |')
    print('----------------------')
    print('    |      |')
    print("", board[4], ' | ', board[5], "", ' | ', board[6])
    print('    |      |')
    print('----------------------')
    print('    |      |')
    print("", board[1], ' | ', board[2], "", ' | ', board[3])
    print('    |      |')


def marker():
    for rep in range(1, 10):

        print("please type 1 for X and 2 for O")
        j = int(input("type 1 or 2"))

        if j == 1:
            global p
            p = "X"


        elif j == 2:

            p = "O"

        else:
            print("please type in 1 and 2 only")
            continue

        print("please tell the position of the tic or toe")

        b = int(input("tell the position of tic or toe"))

        for num in range(1, 10):
            u = b / num
            if u == 1:
                global board
                board[b] = p
            else:
                pass

        display_board(board)

        if board[7] and board[8] and board[9] == p:
            print("we have a winner")

        elif board[4] and board[5] and board[6] == p:
            print("we have a winner")

        elif board[1] and board[2] and board[3] == p:
            print("we have a winner")

        elif board[7] and board[4] and board[1] == p:
            print("we have a winner")

        elif board[8] and board[5] and board[2] == p:
            print("we have a winner")

        elif board[9] and board[6] and board[3] == p:
            print("we have a winner")

        elif board[1] and board[5] and board[9] == p:
            print("we have a winner")

        elif board[3] and board[5] and board[7] == p:
            print("we have a winner")

        else:
            continue


marker()
