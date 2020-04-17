# --------------------------------------------------------------------------
#                         app Tic Tac Toe v1.00
#                 writed by Dominik Lach, Piotr Młudzik
# --------------------------------------------------------------------------

import os
import random


# ------------------------------ functions ---------------------------------

def get_game_mode():
    game_mode=""
    while game_mode not in ["hh", "ah", "ha", "aa"]:
        os.system('clear')  # clear console screen
        print("Possible game mode: hh (human-human) | ah (ai-human) | ha (human-ai)")

        game_mode=input("Choice game mode: ").lower()
        if game_mode=="quit":
            exit()  # ends programm
    return game_mode


def init_board():
    """Returns an empty 3-by-3 board (with zeros)."""
    board={"A":{"1":".", "2":".", "3":"."}, "B":{"1":".", "2":".", "3":"."}, "C":{"1":".", "2":".", "3":"."}}
    return board


def get_move(columns, raws):
    """Returns the coordinates of a valid move for player on board."""
    print("Give coordynates (player " + player + "):")
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
            print("There are only 3 columns: A, B and C")
        elif str(shoot[1])not in columns:
            print("There are only 3 raws: 1, 2 and 3")
        else:
            raw=(shoot[0].upper())
            col=shoot[1]
            return raw, col


def mark(board, player, shoot, n):
    """Marks the element at row & col on the board for player."""
    if board[shoot[0]][shoot[1]]==".":
        if player=="X":
            board[shoot[0]][shoot[1]]="X"
        else:
            board[shoot[0]][shoot[1]]="O"
        n=n*(-1)
        return board, n
    else:
        print("That place is alredy taken")
        return board, n


def raw_win(columns, board, player):
    for n in raws:
        raw=dic_to_list(board, n, columns)
        if raw.count(player)==2 and "." in raw:
            return n, columns[raw.index(".")]


def column_win(raws, board, player):
    for n in columns:
        col=dic_to_list(board, raws, n)
        if col.count(player)==2 and "." in col:
            return raws[col.index(".")] ,n


def diagon_win(columns, raws, board, player):
    diagon=dic_to_list(board, raws, columns)
    if diagon[0].count(player)==2 and "." in diagon[0]:
        return raws[diagon[0].index(".")],columns[diagon[0].index(".")]
    if diagon[1].count(player)==2 and "." in diagon[1]:
        raw=raws[diagon[1].index(".")]
        col=columns[diagon[1].index(".")]
        if raw=="B":
            return raw, col
        if raw=="A":
            raw="C"
            return raw, col
        if raw=="C":
            raw="A"
            return raw, col


def get_ai_move(columns, raws, board, players, m):
    """Returns the coordinates of a valid move for player on board."""
    ai_players=players[:]
    player=ai_players[m]
    cell=diagon_win(columns, raws, board, player)
    if cell==None:
        cell=raw_win(columns, board, player)
    if cell==None:
        cell=column_win(raws, board, player)
    del ai_players[m]
    player=ai_players[0]
    if cell==None:
        cell=diagon_win(columns, raws, board, player)
    if cell==None:
        cell=raw_win(columns, board, player)
    if cell==None:
        cell=column_win(raws, board, player)   
    if cell==None:
        a=random.randint(0,2)
        b=random.randint(0,2)
        raw=raws[a]
        col=columns[b]
        return raw, col
    return cell[0], cell[1]


def dic_to_list(board, x, y):
    lista=[]
    for i in x:
        for n in y:
            lista=lista+[board[i][n]]
    if len(lista)<4:
        return lista
    else:
        diag=[lista[0]]+[lista[4]]+[lista[8]]
        diag2=[lista[6]]+[lista[4]]+[lista[2]]
        return diag, diag2


def has_won(board, player, shoot, raws, columns):
    """Returns True if player has won the game."""
    perp=dic_to_list(board, raws, shoot[1])
    horizon=dic_to_list(board, shoot[0], columns)
    diag=dic_to_list(board, raws, columns)
    if perp==[player, player, player] or horizon==[player, player, player] or diag[0]==[player, player, player] or diag[1]==[player, player, player]:
        return True
    return False


def is_full(board, raws, columns):
    """Returns True if board is full."""
    for i in raws:
        for n in columns:
            if board[i][n]==".":
                return False
    return True


def board_line():
    print("  ---+---+---")


def board_row(letter):
    print(letter + "  " + " | ".join(dic_to_list(board, letter, columns)))


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    print("   " + "   ".join(columns))
    for a in raws:
        board_row(a)
        if a != "C":
            board_line()


# ----------------------------- main code ----------------------------------

if __name__ == '__main__':
    game_mode=""
    raws=["A","B","C"]
    columns=["1","2","3"]
    players=["X","O"]
    n=1
    board_full=""
    win=""

    game_mode=get_game_mode()
    board=init_board()
    while board_full!=True and win!=True:
        os.system('clear')  # clear console screen
        print_board(board)

        if n>0:
            player=players[1]
            if game_mode[0]=="a":
                shoot=get_ai_move(columns, raws, board, players, players.index(player))
            else:
                shoot=get_move(columns, raws)
        else:
            player=players[0]
            if game_mode[1]=="a":
                shoot=get_ai_move(columns, raws, board, players, players.index(player))
            else:
                shoot=get_move(columns, raws)
        if shoot=="quit":
            break

        n=mark(board, player, shoot, n)[1]
        board_full=is_full(board,raws, columns)
        win=has_won(board, player, shoot, raws, columns)

    os.system('clear')  # clear console screen
    print_board(board)
    if board_full and win==False:
        print("It's a tie!")
    if win:
        print(player + " won!")
