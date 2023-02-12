import math
def czy_pierwsza(liczba):
    if liczba == 2 or liczba == 3:
        return True
    if liczba %2 == 0 or liczba%3==0 or liczba<=1:
        return False
    i=5
    while int(math.sqrt(liczba))+1>i:
        if liczba%i == 0:
            return False
        i+=2
        if liczba%i == 0:
            return False
        i+=4
    return True

def mask(liczba):
    wynik=0
    p=0
    while liczba>0:
        wynik=(liczba%2)*10**p+wynik
        liczba//=2
        p+=1
    return wynik

def ile_jedynek(liczba):
    licznik=0
    while liczba>0:
        if liczba%10==1:
            licznik+=1
        liczba//=10
    return licznik

def divide(liczba):
    dl=0
    l_copy=liczba
    while l_copy>0:
        dl+=1
        l_copy//=10
    for i in range(2**(dl-1),2**dl):
        maska=mask(i)
        l_copy=liczba
        if czy_pierwsza(ile_jedynek(maska)):
            wartosc=0
            p=0
            while l_copy>0:
                wartosc=(l_copy%10)*10**p+wartosc
                p+=1
                l_copy//=10
                if maska%10==1 or l_copy==0:
                    if not czy_pierwsza(wartosc):
                        break
                    p=0
                    wartosc=0
                maska//=10
                if l_copy==0:
                    return True
    return False

print(divide(2347))
print(divide(2255))

