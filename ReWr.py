def min(x, y):
    if x>y:
        return y
    else:
        return x

def max(x, y):
    if x>y:
        return x
    else:
        return y

def leng(x, y):
    return len(str(x)), len(str(y))

def multiply(x, y):
    m=0
    while y>0:
        m=m+x
        y=y-1
    return m    


def pow(x, y):
    if y==0:
        return 1
    else:
        m=1
        while y>1:
            m=m*x
            y=y-1
        return m

def divmod(x, y):
    if y==0:
        return "Nie można dzielić przez 0"
    else:
        m=0
        while x>=y:
            x=x-y
            m=m+1
        return(m, x)


print("Podaj dwie liczby. Po każdej naciśnij 'enter'.")
x=int(input())
y=int(input())
print("Mniejsza liczba to: ", min(x, y))
print("Większa liczba to: ", max(x, y))
print("Długość liczb to odpowiedznio: ", leng(x, y))
print("Iloczyn tych liczb to: ", multiply(x, y))
print("Pierwsza liczba do potęgi (druga liczba): ", pow(x, y))
print("Pierwsza liczba podzielona przez drugą daje: ", divmod(x, y), " reszty")