import sys

def hello():
    print("Hello, World!")

def hi(name):
    if (name == ""):
        hello()
    else:
        print("Hello "+ name +"!")
names=["Hello: "]

if len(sys.argv)>1:
    for n in range(1, len(sys.argv)):
        names.append(str(sys.argv[n]))
    print(*names, sep=" ") 
    for n in range(1, len(sys.argv)):
        print("Hello " +str(sys.argv[n]))
else:
    print("Jak masz na imię?")
    name=input()
    hi(name)    