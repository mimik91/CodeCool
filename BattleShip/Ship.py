import os


clear = lambda: os.system('clear') #on Linux System
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def board_generator(size):
    raw=[]
    board=[]
    for _ in range (0,size):
        raw=raw+["0"]
    for _ in range (0,size):
        board=board+[raw.copy()]
    print_board(board)
    return(board)
    

def get_rows_columns(size):
    raws=[]
    columns=[]
    for n in range(0,size):
        raws=raws+[alphabet[n]]
        columns=columns+[str(n+1)]
    return raws, columns



def print_board(lista):
    clear()
    print(" "," ".join(columns))
    for raw in range(0,len(lista)):
        print(raws[raw]," ".join(lista[raw]))


def point_field():
    while True:
        shoot=input()
        if shoot.lower()=="quit":
            return "quit"
        elif len(shoot)!=2:
            print("You can give only one letter followed with one number")
        elif shoot[0].isalpha() != True:
            print("You can give only one letter followed with one number")
        elif shoot[1].isnumeric() != True:
            print("You can give only one letter followed with one number")
        elif shoot[0].upper()not in raws:
            print("There are only",len(columns),"columns:", ",".join((columns)))
        elif str(shoot[1])not in columns:
            print("There are only",len(raws),"raws:", ",".join(raws))
        else:
            raw=(shoot[0].upper())
            col=shoot[1]
            return(raw, col)


def ship_placement(ships_type, table):
    for ship in ships:
        n=int(ships_type[ship])
        while n>0:
            field=point_field()
            raw=int(raws.index(field[0]))
            col=int(field[1])-1
            if table[raw][col]=="0":
                table[raw][col]="X"
                buffer_placment(raw, col, table)
                n=n-1
                print_board(table)
            else:
                print_board(table)
                print("Ships are too close!")


def buffer_placment(raw, col, table): ## buffer field around placed ship
    if str(raw) in columns:
        table[raw - 1][col] = "#"
    if str(col + 2) in columns:
        table[raw][col + 1] = "#"
    if str(col) in columns:
        table[raw][col - 1] = "#"
    if str(raw + 2) in columns:
        table[raw + 1][col] = "#"


def shooting(table, empty_table, player):
    while True:
        field=point_field()
        raw=int(raws.index(field[0]))
        col=int(field[1])-1
        if table[raw][col]=="X":
            empty_table[raw][col]="H"
            print_board(empty_table)
            print("You've sunk a ship!")
            if player==1:
                good_hits[0]=good_hits[0]+1
                if good_hits[0]==3:
                    break
            else:
                good_hits[1]=good_hits[1]+1
                if good_hits[1]==3:
                    break
        elif table[raw][col]=="H":
            print("Sorry, You already shoot at this spot")
            print_board(empty_table)
        else:
            empty_table[raw][col]="M"
            print("You've missed!")
            print_board(empty_table)
            break






size=5

ships_type={"big":2, "small":1}
ships=["small","small","small"]
player=1
good_hits=[0,0]




raws=get_rows_columns(size)[0]
columns=get_rows_columns(size)[1]
board=board_generator(size)
player1_board=board.copy()
print("Player 1: Place your ships on the board")
ship_placement(ships_type, player1_board)
player2_board=board_generator(size)
print("Next player's placement phase")
input("press Enter to contunue")
print("Player 2: Place your ships on the board")
ship_placement(ships_type, player2_board)
player1_shoot_board=board_generator(size)
player2_shoot_board=board_generator(size)
while True:
    if player>0:
        print_board(player1_shoot_board)
        print("Player 1 is shooting")
        shooting(player2_board, player1_shoot_board, 1)
    else:
        print_board(player2_shoot_board)
        print("Player 2 is shooting")
        shooting(player1_board, player2_shoot_board, 2)
    player=player*-1
    if good_hits[0]==3:
        print("Player 1 WON!")
        break
    elif good_hits[1]==3:
        print("Player 2 WON!")
        break