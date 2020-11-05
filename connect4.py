board = []
def create_board(row,col):
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append("")
        board.append(temp)

def visual_board(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j < len(arr[i])-1:
                if arr[i][j] != "":
                    print(arr[i][j],end=" | ")
                else:
                    print(arr[i][j],end="  | ")
            else:
                print(arr[i][j],end="")
        print("")
        rip = "----"*len(arr)
        print(rip)

 
row =''
col = ''

while(True):
    print("Row and column min 4")
    row = int(input('Row for board : '))
    col = int(input('Column for board : '))
    if row >= 4 and col >=4:
        create_board(row,col)
        break

player = 1
turn = 'X'
while(True):
    print("player "+str(player)+" turn")
    while(True):
        col_select = int(input('Choose column : '))
        if col_select > col:
            print("out of range")
        else:
            full = False
            for i in range(row-1,-1,-1):
                if board[i][col_select-1] == '':
                    board[i][col_select-1] = turn
                    x = i
                    y = col_select-1
                    break
                if i==0:
                    full = True
                    print("this column is full")
            if full==False:
                break
    visual_board(board)
    status = ''
    for x in range(col):
        for y in range(row):
            try:
                if board[y][x] == turn and board[y][x+1] == turn and board[y][x+2] == turn and board[y][x+3] == turn:
                    print("player "+ str(player)+" win")
                    status = 'menang'
                elif board[y][x] == turn and board[y+1][x] == turn and board[y+2][x] == turn and board[y+3][x] == turn:
                     print("player "+ str(player)+" win")
                     status = 'menang'
                elif board[y][x] == turn and board[y+1][x+1] == turn and board[y+2][x+2] == turn and board[y+3][x+3] == turn:
                     print("player "+ str(player)+" win")
                     status = 'menang'
                elif board[y][x] == turn and board[y+1][x-1] == turn and board[y+2][x-2] == turn and board[y+3][x-3] == turn:
                     print("player "+ str(player)+" win")
                     status = 'menang'
            except IndexError:
                next
    if status == "menang":
        break
    if player == 1:
        player = 2
        turn = 'O'
    else:
        player = 1
        turn = 'X'
    
    
