import math
def rotuj(liczba):
    cyfra=liczba//10**int((math.log10(liczba)))
    liczba=liczba%10**int((math.log10(liczba)))
    liczba*=10
    liczba+=cyfra
    return liczba

def czy_pierwsza(liczba):
    if liczba==2 or liczba==3:
        return True
    if liczba<2 or liczba%2==0 or liczba%3==0:
        return False
    i=5
    while liczba<int(math.sqrt(liczba))+1:
        if liczba%i==0:
            return False
        i+=2
        if liczba%i==0:
            return False
        i+=4
    return True

def fun(liczba):
    dl=int(math.log10(liczba))+1
    for system in range(2,17):
        for _ in range(dl):
            liczba=rotuj(liczba)
            liczba_copy=liczba
            iloczyn=1
            while liczba_copy>0:
                iloczyn*=liczba_copy%system
                liczba_copy//=system
            if czy_pierwsza(iloczyn):
                return system

    return None
