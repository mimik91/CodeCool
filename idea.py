import sys

f=open("idea.txt", "a")
f.close()
f=open("idea.txt", "r")
tekst=f.read()
lista=tekst.split(",")
if lista[0]=="":
    lista=[]
else:
    lista=lista    
f.close()
if len(sys.argv)==2:
    inter=sys.argv[1]
    if inter=="--list":
        print("Twoje aktualne idee:")
        for n in range(0,len(lista)):
            print(n+1, ". " ,lista[n])
else:
    if len(sys.argv)>1:
        inter=sys.argv[1]
        inter2=sys.argv[2]
        if inter=="--delete" and int(inter2)>0 and int(inter2)<int(len(lista)+1):
            del lista[int(inter2)-1]
if len(sys.argv)<2:
    while True:
        print("Twoje aktualne idee:")
        for n in range(0,len(lista)):
            print(n+1, ". " ,lista[n])
        print("What is Your new idea?")
        added=input()
        if added=="break":
            break
        lista=lista+[added]
f=open("idea.txt", "w")
f.write(",".join(lista))
f.close()