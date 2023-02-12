import math
def czy_pierwsza(liczba):
    if liczba==2 or liczba==3:
        return True
    if liczba%2==0 or liczba%3==0 or liczba<2:
        return False
    i=5
    while i<math.sqrt(liczba)+1:
        if liczba%i==0:
            return False
        i+=2
        if liczba%i==0:
            return False
        i+=4
    return True


def fun(tab):
    iloczyn=1
    for i in tab:
        if czy_pierwsza(i):
            iloczyn*=i
    i=len(tab)-1
    while i>=0:
        if czy_pierwsza(tab[i]):
            iloczyn//=tab[i]
        if tab[i]==iloczyn:
            return i
        i-=1
    return None


tab=[2,3,4,50,6]
print(fun(tab))