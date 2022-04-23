from UI import header
# Kumpulan Fungsi dan Prosedur

#Menampilkan status papan
def showPapan():
    print("Board status: ")
    for i in range (3):
        for j in range (3):
            if j!=2:
                print(papan[i][j], end="")
            else:
                print(papan[i][j])
    print()

#Menentukan jika ada pemain sudah ada yg menang
def winningState():
    #Inisialisasi
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

#Menentukan apakah papan sudah penuh
def full():
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

header("TIC TAC TOE")
###########################################################################

#Algoritma Utama

#Tampilan pesan awal
print("Welcome to Tic Tac Toe!")

#Meminta input nama pemain
print("Please input your names!")
player1=input("Player 1 (X): ")
player2=input("Player 2 (O): ")

#Inisialisasi papan
print("Let the game start!")
papan=[["#" for i in range (3)]for i in range (3)]
turns=1

#Pengisian papan
while True:
    showPapan()
    #Menentukan apakah giliran pemain 1 atau 2
    if turns%2==1:
        print(player1 + "'s (X) turn!")
    else:
        print(player2 + "'s (O) turn!")
    
    #Mengisi kotak papan dan akan mengullang terus hingga input valid
    while True:
        #Meminta koordinat kotak yang ingin diisi
        print("Type the coordinates: ")
        X=int(input("X: "))
        Y=int(input("Y: "))

        #Menentukan apakah input valid atau tidak
        if X>3 or X<=0 or Y>3 or Y<=0:
            print("Invalid coordinates! Please try again\n")
        #Menentukan apakah kotak sudah diisi atau belum
        elif papan[Y-1][X-1]=="X" or papan[Y-1][X-1]=="O":
            print("Coordinates already used! Please try again\n")
        else:
            break
    
    #Mengisi kotak bergantung pada giliran pemain
    if turns%2==1:
        papan[Y-1][X-1]="X"
    else:
        papan[Y-1][X-1]="O"
    
    #Menentukan kondisi permainan
    if winningState()=="X":
        print()
        print(player1, "(X) WINS!")
        break
    elif winningState()=="O":
        print()
        print(player2, "(O) WINS!")
        break
    else:
        #Menentukan apakah papan penuh atau tidak
        if full():
            showPapan()
            print("Its a TIE!")
            break
        else:
            turns+=1

