import math
def warunek(iloczyn,liczba):
    k=2
    if iloczyn%liczba==0:
        return False
    while k<=int(math.sqrt(liczba))+1:
        if liczba%k==0 and iloczyn%k==0:
            return False
        k+=1
    return True

def fun(t):
    n=len(t)
    lewy=0
    prawy=1
    iloczyn=t[0]
    najdluzszy=0
    dlugosc=1
    while prawy<n:
        if warunek(iloczyn,t[prawy]):
            iloczyn*=t[prawy]
            dlugosc+=1
            prawy+=1
        else:
            iloczyn//=t[lewy]
            dlugosc-=1
            lewy+=1
        najdluzszy=max(dlugosc,najdluzszy)

    return najdluzszy

t=[2,23,33,35,7,4,6,7,5,11,13,22]
print(fun(t))