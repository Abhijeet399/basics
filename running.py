board=[" "]*10

def display_board(board):

    print('    |      |')
    print("" ,  board[7] , ' | ' , board[8] ,"" ,  ' | ' , board[9])
    print('    |      |')
    print('----------------------')
    print('    |      |')
    print( "" , board[4] , ' | ' , board[5] ,"" ,  ' | ' , board[6])
    print('    |      |')
    print('----------------------')
    print('    |      |')
    print("" ,  board[1] , ' | ' , board[2] ,"" ,  ' | ' , board[3])
    print('    |      |')



def marker():
    print("please type 1 for X and 2 for O")
    j = int(input("type 1 or 2"))

    if j == 1:

        l = "X"


    elif j == 2:

        l = " O "

    else:
        print("please type in 1 and 2 only")

    print("please tell the position of the tic or toe")

    b=int(input("tell the position of tic or toe"))

    for num in range(1,10):
        u=b/num
        if u==1:
            global board
            board[b]=l
        else:
            print("something is wrong")



    display_board(board)




marker()



