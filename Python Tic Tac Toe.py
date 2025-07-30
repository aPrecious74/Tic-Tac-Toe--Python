import copy
from random import randrange

board=[
        [("-") for i in range(8)],
        [(" ") for j in range(8)],
        [(" ") for j in range(8)],
        [(" ") for j in range(8)],
            ]
board[0][0]="+"
board[1][0]=board[2][0]=board[3][0]="|"
#individual board sections
topLB=copy.deepcopy(board)
#_1=topLB[2][4]
topMB=copy.deepcopy(board)
#_2=topMB[2][4]
topRB=copy.deepcopy(board)
#_3=topRB[2][4]
MidLB=copy.deepcopy(board)
#_4=MidLB[2][4]
MidMB=copy.deepcopy(board)
#_5=MidMB[2][4]
MidRB=copy.deepcopy(board)
#_6=MidRB[2][4]
BotLB=copy.deepcopy(board)
#_7=BotLB[2][4]
BotMB=copy.deepcopy(board)
#_8=BotMB[2][4]
BotRB=copy.deepcopy(board)
#_9=BotRB[2][4]
SidePiece=[["+"], ["|"], ["|"], ["|"]]
BottomPiece=[["+"],["-"],["-"],["-"],["-"],["-"],["-"],["-"]]
global usable_area_in_board
usable_area_in_board=[topLB[2][4],topMB[2][4],topRB[2][4],MidLB[2][4],MidMB[2][4],MidRB[2][4],BotLB[2][4],BotMB[2][4],BotRB[2][4]]
full_board=[topLB,topMB,topRB,MidLB,MidMB,MidRB,BotLB,BotMB,BotRB]
def boards():
    for elem in range(4):
        print(*topLB[elem],*topMB[elem],*topRB[elem],*SidePiece[elem])
    for elem in range(4):
        print(*MidLB[elem],*MidMB[elem],*MidRB[elem],*SidePiece[elem])
    for elem in range(4):
        print(*BotLB[elem],*BotMB[elem],*BotRB[elem],*SidePiece[elem])
    for elem in range(3):
        for elem in BottomPiece:
            print(*elem, end=" ")
    print("+")

    
def make_list_of_free_fields(spaceAvailable):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    global free_fields
    free_fields=[]
    for elem in usable_area_in_board:
        if elem=="O" or elem=="X":
            free_fields.append(1)
        else: free_fields.append(0)

def draw_move(spaceAvailable):
    # The function draws the computer's move and updates the board.
    MoveForward=False
    print("Computer's turn...", "\n")
    make_list_of_free_fields(usable_area_in_board)
    while MoveForward==False:
        Cplay=randrange(1,10)
        if free_fields[Cplay-1]==1:
            continue
        else: MoveForward=True
    print("Computer plays: ", Cplay)
    MoveForward=False
    if Cplay==1:
        topLB[2][4]= "X"
        MoveForward=True 
    if Cplay==2:
        topMB[2][4]= "X"
        MoveForward=True
    if Cplay==3:
        topRB[2][4]= "X"
        MoveForward=True
    if Cplay== 4:
        MidLB[2][4]= "X"
        MoveForward=True
    if Cplay== 5:
        MidMB[2][4]= "X"
        MoveForward=True
    if Cplay==6:
        MidRB[2][4]= "X"
        MoveForward=True
    if Cplay==7:
        BotLB[2][4]= "X"
        MoveForward=True
    if Cplay== 8:
        BotMB[2][4]= "X"
        MoveForward=True
    if Cplay==9:
        BotRB[2][4]= "X"
        MoveForward=True
    if MoveForward:
        usable_area_in_board[Cplay-1]="X"
        boards()
        if not victory_for("X"):
            enter_move(board,spaceAvailable)
        else: play_again()

def enter_move(board,spaceAvailable):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    MoveForward=False
    while True:
        try:
            UserMove= int(input("Enter your move(1-9):"))
            if free_fields[UserMove-1]==1:
                print("Please draw a field that has not been played")
                continue
            if UserMove==1:
                topLB[2][4]= "O"
                MoveForward=True 
            elif UserMove==2:
                topMB[2][4]= "O"
                MoveForward=True
            elif UserMove==3:
                topRB[2][4]= "O"
                MoveForward=True
            elif UserMove== 4:
                MidLB[2][4]= "O"
                MoveForward=True
            elif UserMove== 5:
                MidMB[2][4]= "O"
                MoveForward=True
            elif UserMove==6:
                MidRB[2][4]= "O"
                MoveForward=True
            elif UserMove==7:
                BotLB[2][4]= "O"
                MoveForward=True
            elif UserMove== 8:
                BotMB[2][4]= "O"
                MoveForward=True
            elif UserMove==9:
                BotRB[2][4]= "O"
                MoveForward=True
            if MoveForward:
                break
        except:
                print("Please enter a correct integer value")
    usable_area_in_board[UserMove-1]="O"
    boards()
    if not victory_for("O"):
        draw_move(make_list_of_free_fields)
    else: play_again()


def victory_for(sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    make_list_of_free_fields(usable_area_in_board)
    Tie=all(free_fields)
    if (topLB[2][4]==sign and topMB[2][4]==sign and topRB[2][4]==sign)or \
    (MidLB[2][4]==sign and MidMB[2][4]==sign and MidRB[2][4]==sign)or \
    (BotLB[2][4]==sign and BotMB[2][4]==sign and BotRB[2][4]==sign)or\
    (topLB[2][4]==sign and MidMB[2][4]==sign and BotRB[2][4]==sign)or\
    (BotLB[2][4]==sign and MidMB[2][4]==sign and topRB[2][4]==sign)or\
    (topLB[2][4]==sign and MidLB[2][4]==sign and BotLB[2][4]==sign)or\
    (topMB[2][4]==sign and MidMB[2][4]==sign and BotMB[2][4]==sign)or\
    (topRB[2][4]==sign and MidRB[2][4]==sign and BotRB[2][4]==sign):
        if sign=="O":
            sign= "You"
        elif sign=="X": sign="Computer"
        print(sign, "won!")
        return True
    elif Tie:
        print("Nobody won! Better luck next time...")
        return True
    else:
        return False
def first_play():
    print("Computer plays first")
    MidMB[2][4]= "X"
    usable_area_in_board[5-1]="X"
    make_list_of_free_fields(usable_area_in_board)
    boards()
    enter_move(boards,usable_area_in_board)
def play_again():
    while True:
        answer=input("Would you like to play again? (Y or N): ")
        if answer == "Y":
            print("\n","(playing again...)","\n")
            for i in full_board:
                i[2][4]=" "
            for elem in range(len(usable_area_in_board)):
                usable_area_in_board[elem]=" "
            first_play()
        elif answer== "N": return
        else:
            print("Type 'Y' or 'N' as your response")
first_play()
