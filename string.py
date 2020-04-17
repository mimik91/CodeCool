import math
alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def get_list(tekst):
    badana=[]
    for i in range(0, len(tekst)):
        if tekst[i].isalpha()==True:
            badana=badana+[tekst[i].upper()]
    return badana


def is_palindrome(tested):
    for n in range (0, int(math.ceil(len(tested)/2))):
        if tested[n]!=tested[-(n+1)]:
             return False       
    return True
        

def is_isogram(tested):
    u=1
    for n in tested:
        k=u    
        for i in range(k,len(tested)):
            k=k+1
            if n==tested[i]:
                return False
        u=u+1
    return True

def is_pangram(tested, alphabet):
    n=len(alphabet)
    for i in range(0,len(alphabet)):
        if alphabet[i] in tested:
            n=n-1
        if n==0:
            return True
    return False, n

def is_anagram(tested, tested2):
    if len(tested)==len(tested2):
        if is_pangram(tested, tested2)==True:
            return True
        if is_pangram(tested, tested2)[1]<2:
            return "Is blanagram"
    return False

 


tekst=input()
tested=get_list(tekst)
print(is_palindrome(tested))
print(is_isogram(tested))
print(is_pangram(tested, alphabet)[0])
tekst=input()
tested2=get_list(tekst)
print(is_anagram(tested, tested2))
