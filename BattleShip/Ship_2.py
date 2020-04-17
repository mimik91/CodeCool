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

def possible_coordinates(raw, col, table):
    cordinates_list = []
    if str(raw) in columns and table[raw - 1][col] == '0':
        cordinates = coordinate_conversion(raw - 1, col)                    
        cordinates_list = cordinates_list + [cordinates]
    if str(col + 2) in columns and table[raw][col + 1] == '0':
        cordinates = coordinate_conversion(raw, col + 1)
        cordinates_list = cordinates_list + [cordinates]
    if str(col) in columns and table[raw][col - 1] == '0':
        cordinates = coordinate_conversion(raw, col - 1)
        cordinates_list = cordinates_list + [cordinates]
    if str(raw + 2) in columns and table[raw +1][col] == '0':
        cordinates = coordinate_conversion(raw + 1, col)
        cordinates_list = cordinates_list + [cordinates]
    return cordinates_list



def ship_placement(ships_type, table):
    for ship in ships:
        n=int(ships_type[ship])
        if n == 2:
            while True:
                field=point_field()
                raw=int(raws.index(field[0]))
                col=int(field[1])-1
                if table[raw][col] != '0':
                    print("Ships are to close !")
                else:
                    cordinates_list=possible_coordinates(raw, col, table)
                    if cordinates_list == []:
                        print("There is no place here for a big ship!")
                    else:
                        print("Possible coordinates for placment of big ship are:  ")
                        for cordinates in cordinates_list:
                            print("".join(cordinates))

                    field_2 =  []   
                    point = point_field()
                    field_2 = [point[0], point[1]]
                    if field_2 not in cordinates_list:
                        print("You chose wrong coordinates. Possible coordinates for placment of big ship are:  ")
                        for cordinates in cordinates_list:
                            print("".join(cordinates))
                    else:
                        raw_2=int(raws.index(field_2[0]))
                        col_2=int(field_2[1]) - 1
                        table[raw][col]="X"
                        table[raw_2][col_2]="X"
                        buffer_placment(raw, col, table)
                        buffer_placment(raw_2, col_2, table)
                        print_board(table)
                        break
        else:
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

def coordinate_conversion(raw, col):
    conversion_value = []
    conversion_value = [raws[raw], columns[col]]
    return conversion_value
    

def buffer_placment(raw, col, table): ## buffer field around placed ship
    
    if str(raw) in columns and table[raw - 1][col] == '0':
        table[raw - 1][col] = "#"
    if str(col + 2) in columns and table[raw][col + 1] == '0':
        table[raw][col + 1] = "#"
    if str(col) in columns and table[raw][col - 1] == '0':
        table[raw][col - 1] = "#"
    if str(raw + 2) in columns and table[raw +1][col] == '0':
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


def get_size():
    print("Your board can have from 3 to 9 rows. How big board You choose?")
    while True:
        size=int(input())
        if size in [3, 4, 5, 6, 7, 8, 9]:
            return size
        else:
            print("Give only one number form 3 to 9 as size")


def ships_amount():
    print("You can choose from big and small ships. Small ships take one spot, big ships take two spots")
    print("How many big ships?")
    ships=[]
    while True:
        amount=int(input())
        if amount in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            for _ in range(0,amount):
                ships=ships+["big"]
            break
        else:
            print("Give only one number form 1 to 9 as amount")
    print("How many small ships?")
    while True:
        amount=int(input())
        if amount in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            for _ in range(0,amount):
                ships=ships+["small"]
            break
        else:
            print("Give only one number form 1 to 9 as amount")
    print(ships)
    return(ships)

        

size=get_size()

ships_type={"big":2, "small":1}
ships=ships_amount()
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