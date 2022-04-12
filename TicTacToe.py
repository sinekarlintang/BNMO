def showPapan():
    print("Board status: ")
    for i in range (3):
        for j in range (3):
            if j!=2:
                print(papan[i][j], end="")
            else:
                print(papan[i][j])
    print()

def winningState():
    XWin=["X", "X", "X"]
    OWin=["O", "O", "O"]
    winX=False
    winO=False
    
    #Horizontal
    for i in range (3):
        if papan[i]==XWin:
            winX=True
        elif papan[i]==OWin:
            winO=True
    
    #Vertikal
    tempVer=["" for i in range (3)]
    i=0
    while i<3 and winX==False and winO==False:
        for j in range (3):
            tempVer[j]=papan[j][i]

        if tempVer==XWin:
            winX=True
            break
        elif tempVer==OWin:
            winO=True
            break
        else:
            i+=1
    
    #Diagonal
    tempDia1=[papan[0][0], papan[1][1], papan[2][2]]
    tempDia2=[papan[0][2], papan[1][1], papan[2][0]]

    if tempDia1==XWin or tempDia2==XWin:
        winX=True
    elif tempDia1==OWin or tempDia2==OWin:
        winO=True
    
    if winX==True:
        return "X"
    elif winO==True:
        return "O"
    else:
        return "#"

def penuh():
    count=0
    for i in range (3):
        for j in range (3):
            if papan[i][j]=="#":
                count+=1
    
    if count==0:
        finish=True
    else:
        finish=False
        
    return finish

###########################################################################

print("Welcome to Tic Tac Toe!")
print("Please input your names!")
player1=input("Player 1 (X): ")
player2=input("Player 2 (O): ")
print("Let the game start!")

papan=[["#" for i in range (3)]for i in range (3)]
turns=1
while True:
    showPapan()
    if turns%2==1:
        print(player1 + "'s (X) turn!")
    else:
        print(player2 + "'s (O) turn!")
    
    while True:
        print("Type the coordinates: ")
        X=int(input("X: "))
        Y=int(input("Y: "))
        if X>3 or X<=0 or Y>3 or Y<=0:
            print("Invalid coordinates! Please try again\n")
        elif papan[Y-1][X-1]=="X" or papan[Y-1][X-1]=="O":
            print("Coordinates already used! Please try again\n")
        else:
            break

    if turns%2==1:
        papan[Y-1][X-1]="X"
    else:
        papan[Y-1][X-1]="O"
    
    #Kondisi permainan
    if winningState()=="X":
        print()
        print(player1, "(X) WINS!")
        break
    elif winningState()=="O":
        print()
        print(player2, "(O) WINS!")
        break
    else:
        if penuh():
            showPapan()
            print("Its a TIE!")
            break
        else:
            turns+=1

