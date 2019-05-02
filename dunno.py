def win_check(board, player):

    if board[7]  ==  board[8] ==  board[9] == player:
        print("we have a winner")
        return True
    elif board[4] ==  board[5] ==  board[6] == player:
        print("we have a winner")
        return True
    elif board[1] ==  board[2] ==  board[3] == player:
        print("we have a winner")
        return True
    elif board[7] ==  board[4] ==  board[1] == player:
        print("we have a winner")
        return True
    elif board[8] ==  board[5] ==  board[2] == player:
        print("we have a winner")
        return True
    elif board[9] ==  board[6] ==  board[3] == player:
        print("we have a winner")
        return True
    elif board[1] ==  board[5] ==  board[9] == player:
        print("we have a winner")
        return True
    elif board[3] ==  board[5] ==  board[7] == player:
        print("we have a winner")
        return True

    else:
        return False