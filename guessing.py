import random

def check(height):
    los = random.randint(1, height)
    shoot=0
    while shoot != los:
        print("Enter an integer from 1 to "+str(height)+": ")
        shoot=int(input())
        print(los, shoot, height)
        if shoot < los:
            print("guess is low")       
        else:
            print("guess is high")

def succes(rounds, n):
    while rounds > 0:
        check(n)
        print("you guessed it!")
        rounds=rounds-1


big=99
small=49
rounds=3
height=[big, small]

for n in height:
    succes(rounds, n)