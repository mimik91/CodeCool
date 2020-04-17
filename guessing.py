import random

def check(height):
    los = random.randint(1, height)
    shoot=0
    while shoot != los:
        print("Enter an integer from 1 to "+str(height-1)+": ")
        try:
            shoot=int(input())
            if shoot < los:
                print("guess is low")       
            else:
                print("guess is high")
        except ValueError:
            print("Insert only numbers")

def succes(rounds, value):
    while rounds > 0:
        check(value)
        print("you guessed it!")
        rounds=rounds-1


big=100
small=50
rounds=2
height=[big, small]

for value in height:
    succes(rounds, value)
