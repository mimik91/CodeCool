import sys
import random

def pick_capital():
    f=open("Hangman.txt", "r")
    tekst=f.read()
    lista=tekst.split("\n")
    los=random.randint(0,len(lista)-1)
    capital=(lista[los])
    capital=capital.upper()
    unhashed=[]
    for n in range(0,len(capital)):
        unhashed=unhashed+[capital[n]]
    return unhashed
    pass


def get_hashed(word):
    hashed=[]
    for n in range(0,len(word)):
        if word[n]==" ":
            hashed=hashed+["   "]
        elif word[n]=="-":
            hashed=hashed+[" - "]
        else:    
            hashed=hashed+["_ "]    
    return hashed
    pass

def uncover(hashed_password, password, letter):
    for n in range(0,len(password)):
        if str(letter)==password[n]:
            hashed_password[n]=password[n]
    return hashed_password
    pass


def update(used_letters, letter):
    if letter in used_letters:
        return used_letters
    else:
        used_letters=used_letters+[letter]
        return used_letters
    pass


def is_win(hashed_password, password):
    if hashed_password==password:
        return True
    pass


def is_loose(life_points):
    if life_points==0:
        return True
    else:
        return False
    pass


def get_input(used_letters):
    while True:
        print("Podaj literę")
        leter=input()
        if leter.isalpha():
            if len(leter)>1:
                print("Podaj tylko jedną literę")
            elif leter.upper() in used_letters:
                print("Już użyłeś tej litery")
            else:
                return(leter.upper())
                pass
        else:
            print("Możesz podać tylko literę")
        
def odmiana(live):
    if live>4:
        return " żyć"
    elif live>1:
        return " życia"
    else:
        return " życie"

def main():
    password=pick_capital()
    hashed_password=get_hashed(password)
    used_letters=[]
    live=10
    while live>0:
        print("masz "+str(live)+ odmiana(live))
        print("".join(hashed_password))
        leter=get_input(used_letters)
        used_letters=update(used_letters,leter)
        print("Zużyte litery: ", ", ".join(used_letters))
        uncover(hashed_password, password, leter)
        if leter not in password:
            live=live-1
        if hashed_password==password:
             print("Brawo, zgadłeś! Wygrałeś życie!")
             break
        if live==0:
            print("You died. You are hanging")
            print("The city was "+"".join(password))
            break


main()


#if __name__ == '__main__':
    #main()