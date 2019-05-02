board = [" "] * 10

def display_board(board):
    print('    |      |')
    print("", board[7], ' | ', board[8], "", ' | ', board[9])
    print('    |      |')
    print('-------------------')
    print('    |      |')
    print("", board[4], ' | ', board[5], "", ' | ', board[6])
    print('    |      |')
    print('-------------------')
    print('    |      |')
    print("", board[1], ' | ', board[2], "", ' | ', board[3])
    print('    |      |')


def marker():
    for rep in range(1, 10):

        print("please type 1 for X and 2 for O")
        j = int(input("type 1 or 2"))

        if j == 1:

            p = "X"


        elif j == 2:

            p = "O"

        else:
            print("please type in 1 and 2 only")
            continue


        print("please tell the position of the tic or toe")

        b = int(input("tell the position of tic or toe"))

        if b>=10 or b==0:
            print("Please enter value between 1 and 9")
            continue
        else:
            pass
        for num in range(1, 20):
            u = b / num
            if u == 1:
                global board
                board[b] = p
            else:
                pass

        display_board(board)

        if board[7] == board[8] == board[9] ==  p:
            print("we have a winner1")

        elif board[4] == board[5] == board[6] ==  p:
            print("we have a winner2")

        elif board[1] == board[2] == board[3] == p:
            print("we have a winner3")

        elif board[7] == board[4] == board[1] == p:
            print("we have a winner4")

        elif board[8] == board[5] == board[2] == p:
            print("we have a winner5")

        elif board[9] == board[6] == board[3] == p:
            print("we have a winner6")

        elif board[1] == board[5] == board[9] == p:
            print("we have a winner7")

        elif board[3] == board[5] == board[7] == p:
            print("we have a winner8")

        else:
            continue


marker()
