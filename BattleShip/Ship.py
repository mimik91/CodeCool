import os
game=[[0,0,1,1],[0,0,1,2],[0,1,1,1],[0,1,2,2],[1,1,1,1],[1,1,1,2],[1,1,2,3]]
ship_size=["big", "medium", "small", "micro"]
ships_type={"big":4, "medium":3, "small":2, "micro":1}


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


def human_to_num(raw, col):
    raw=raws.index(raw)
    col=columns.index(col)
    return raw, col


def num_to_hum(raw, col):
    raw=raws[raw]
    col=columns[col]
    return raw, col


def point_field():
    raw=-1
    while raw == -1:
        shoot=input()
        if shoot.lower()=="quit":
            return "quit"
        elif len(shoot)!=2:
            print("You can give only one letter followed with one number")
        elif not shoot[0].isalpha():
            print("You can give only one letter followed with one number")
        elif not shoot[1].isnumeric():
            print("You can give only one letter followed with one number")
        elif shoot[1] not in columns:
            print("There are only",len(columns),"columns:", ",".join((columns)))
        elif str(shoot[0].upper())not in raws:
            print("There are only",len(raws),"raws:", ",".join(raws))
        else:
            shoot=human_to_num(shoot[0].upper(), shoot[1])
            raw=shoot[0]
            col=shoot[1]
            return raw, col


def possible_coordinates(raw, col, table, n):
    coordinates_list = []
    checker=0
    for m in range(1,n+1):
        if str(raw-m+1) in columns and table[raw - m][col] == '0':
            checker=checker+1
            if checker==n:
                shoot=num_to_hum(raw-1,col)                  
                coordinates_list = coordinates_list + [[shoot[0], shoot[1]]]
    checker=0
    for m in range(1,n+1):
        if str(col +m +1) in columns and table[raw][col + m] == '0':
            checker=checker+1
            if checker==n:
                shoot=num_to_hum(raw,col+1)                  
                coordinates_list = coordinates_list + [[shoot[0], shoot[1]]]
    checker=0
    for m in range(1,n+1):
        if str(col -m +1) in columns and table[raw][col - m] == '0':
            checker=checker+1
            if checker==n:
                shoot=num_to_hum(raw,col-1)                  
                coordinates_list = coordinates_list + [[shoot[0], shoot[1]]]
    checker=0
    for m in range(1,n+1):
        if str(raw +m +1) in columns and table[raw +m][col] == '0':
            checker=checker+1
            if checker==n:
                shoot=num_to_hum(raw+1,col)                  
                coordinates_list = coordinates_list + [[shoot[0], shoot[1]]]
    return coordinates_list


def ships_available(ships_type, table):
    player_ships=[]
    for ship in ships:
        ship_len=int(ships_type[ship])
        player_ship=ship_coordinates(table, ship_len)
        for element in player_ship:
            table[element[0]][element[1]]="X"
        for element in player_ship:
            buffer_placment(element[0],element[1], table)
        player_ships=player_ships+[player_ship]
        print_board(table)
    return player_ships


def ship_coordinates(table, ship_len):
    player_ship=[]
    coordinate_list=[]
    k=ship_len                   
    while ship_len>0:
        field=point_field()
        raw=field[0]
        col=field[1]
        if k>ship_len:
            check=num_to_hum(raw, col)
            check=[check[0],check[1]]
            if check not in coordinate_list:
                print("You can choose only fromy those coordinates:")
                for coordinates in coordinate_list:
                    print("".join(coordinates))
            else:
                change_raw=raw-player_ship[0][0]
                change_col=col-player_ship[0][1]
                for m in range(0,ship_len):
                    player_ship=player_ship+[[player_ship[m][0]+change_raw, player_ship[m][1]+change_col]]
                return player_ship       
        else:
            data=adding_coordinates(raw, col, table, ship_len, player_ship, coordinate_list)
        ship_len=data[0]
        coordinate_list=data[1]
        player_ship=data[2]
    return player_ship


def adding_coordinates(raw, col, table, ship_len, player_ship, coordinate_list):
    if table[raw][col] != '0':
        print_board(table)
        print("Ships are to close !")
    else:
        player_ship=player_ship+[[raw,col]]
        ship_len=ship_len-1
        if ship_len>0:
            coordinate_list=possible_coordinates(raw, col, table, ship_len)
            if coordinate_list==[]:
                print("There is no place here for such a big ship!")
                player_ship=[]
                ship_len=ship_len+1
            else:
                print("Possible coordinates for placment of big ship are:  ")
                for coordinates in coordinate_list:
                    print("".join(coordinates))
    return ship_len, coordinate_list, player_ship
    

def buffer_placment(raw, col, table):
    if str(raw) in columns and table[raw - 1][col] == '0':
        table[raw - 1][col] = "#"
    if str(col + 2) in columns and table[raw][col + 1] == '0':
        table[raw][col + 1] = "#"
    if str(col) in columns and table[raw][col - 1] == '0':
        table[raw][col - 1] = "#"
    if str(raw + 2) in columns and table[raw +1][col] == '0':
        table[raw + 1][col] = "#"


def shooting(table, empty_table):
    while player_hits[player] != player_ships[player]:
        field=point_field()
        raw=field[0]
        col=field[1]
        if empty_table[raw][col]=="H":
            print("Sorry, You already shoot at this spot")
            print_board(empty_table)
        elif table[raw][col]=="X":
            check_hit(raw, col, empty_table)
        else:
            empty_table[raw][col]="M"
            print("You've missed!")
            print_board(empty_table)
            break


def check_hit(raw, col, empty_table):
    for ship in range(0,len(player_ships[player])):
        if [raw,col] in player_ships[player][ship]:
            empty_table[raw][col]="H"
            player_hits[player][ship]=player_hits[player][ship]+[[raw,col]]
            print_board(empty_table)
            print("You have HIT!")
            if sorted(player_hits[player][ship])in player_ships[player]:
                player_hits[player][ship]=sorted(player_hits[player][ship])
                for n in player_hits[player][ship]:
                    empty_table[n[0]][n[1]]="S"
                print_board(empty_table)
                print("You've sunk a ship!")


def get_size():
    print("Your board can have from 3 to 9 rows. How big board You choose?")
    while True:
        size=int(input())
        if size in [3, 4, 5, 6, 7, 8, 9]:
            return size
        else:
            print("Give only one number form 3 to 9 as size")


def get_ship_amount(size):
    ship_amount=[]
    actual_game=game[size-3]
    for ship in range(0, len(actual_game)):
        for n in range(0,actual_game[ship]):
            ship_amount=ship_amount+[ship_size[ship]]
    print("Your ships to place: " ", ".join(ship_amount))
    return ship_amount


def get_ships_to_hits():
    for ship in player_ships[player]:
        player_hits[player]=player_hits[player]+[[]]
    return player_hits[player]



size=get_size()
ships=get_ship_amount(size)
player0_board=[]
player1_board=[]
player0_shoot_board=[]
player1_shoot_board=[]
player0_ships=[]
player1_ships=[]
player0_hits=[]
player1_hits=[]
player_hits=[player0_hits, player1_hits]
player_ships=[player0_ships, player1_ships]
boards=[player0_board, player1_board, player0_shoot_board, player1_shoot_board]
players=[0,1]



raws=get_rows_columns(size)[0]
columns=get_rows_columns(size)[1]
for player in players:
    boards[player]=board_generator(size)
    print("Player",player+1,": Place your ships on the board")
    input("press Enter to contunue")
    player_ships[player]=ships_available(ships_type, boards[player])
    boards[player+2]=board_generator(size)
    player_hits[player]=get_ships_to_hits()

while player_hits[player] != player_ships[player]:
    for player in players:
        print_board(boards[player+2])
        print("Player",player+1,"is shooting")
        shooting(boards[(player+1)%2], boards[player+2])
        if player_hits[player] == player_ships[player]:
            print("Player",player+1, "WON!")
            break