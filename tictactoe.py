player = 1
array = [["","",""],["","",""],["","",""]]

def drawfield(arr):
    for i in range(len(arr)):
        for x in range(len(arr[i])):
            if x % 2 == 0:
                if arr[i][x] == "":
                    print("   ",end="")
                else:
                    print(" "+arr[i][x]+" ",end ="")
            else:
                if arr[i][x] == "":
                    print("| ",end="  |")
                else:
                    print("| "+arr[i][x]+" |",end ="")
                
        print("")
        print("_ _ _ _ _ _")
player = 1
pep = 0
def play():
    global player
    global array
    global pep
    array = [["","",""],["","",""],["","",""]]
    while(True):
        print("players turn : "+str(player))
        row = int(input("please enter row\n")) - 1
        kolom = int(input("please enter kolom\n")) - 1
        inputs = ""
        if player == 1:
            inputs = "X"
        else:
            inputs = "O"
        sep = ""
        sep2 = ""
        if array[row][kolom] != "":
            print("sorry cant enter")
            while(True):
                row2 = int(input("please enter row\n")) - 1
                kolom2 = int(input("please enter kolom\n")) - 1
                if array[row2][kolom2] == "":
                    sep = row2
                    sep2 = kolom2
                    break
            array[sep][sep2] = inputs   
        else:
            array[row][kolom] = inputs
        drawfield(array)
        beb = cek_menang(array)
        if beb == "menang":
            print("player yang menang : "+str(player))
            player = 1
            break
        if player == 1:
            player = 2
        else:
            player = 1
        pep = pep + 1
        if pep == 9:
            print("udah selesai")
            break
        
    

def cek_menang(arr):
    status = ""
    if (arr[0][0] == arr[1][0]) and (arr[0][0] == arr[2][0]) and (arr[0][0] != ""):
        status = "menang"
    elif (arr[0][1] == arr[1][1]) and (arr[0][1] == arr[2][1]) and (arr[0][1] != ""):
        status = "menang"
    elif (arr[0][2] == arr[1][2]) and (arr[0][2] == arr[2][2]) and (arr[0][2] != ""):
        status = "menang"
    elif (arr[0][0] == arr[0][1]) and (arr[0][0] == arr[0][2]) and (arr[0][0] != ""):
        status = "menang"
    elif (arr[1][0] == arr[1][1]) and (arr[1][0] == arr[1][2]) and (arr[1][0] != ""):
        status = "menang"
    elif (arr[2][0] == arr[2][1]) and (arr[2][0] == arr[2][2]) and (arr[2][0] != ""):
        status = "menang"
    elif (arr[0][1] == arr[1][1]) and (arr[0][1] == arr[2][2]) and (arr[0][1] != ""):
        status = "menang"
    elif (arr[0][2] == arr[1][1]) and (arr[0][2] == arr[2][0]) and (arr[0][2] != ""):
        status = "menang"
    return status

play()