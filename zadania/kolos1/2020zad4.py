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

def ile_jedynek(liczba):
    licznik=0
    while liczba>0:
        if liczba%2==1:
            licznik+=1
        liczba//=10
    return licznik

def mask(liczba):
    wynik=0
    p=0
    while liczba>0:
        wynik=liczba%2*(10**p)+wynik
        p+=1
        liczba//=2
    return wynik

def dl(liczba):
    licznik=0
    while liczba>0:
        licznik+=1
        liczba//=10
    return licznik

def divide(N):
    d=dl(N)

    for i in range(2**(d-1),2**d):
        maska=mask(i)

        if czy_pierwsza(ile_jedynek(maska)):
            l_copy=N
            p=0
            wartosc=0
            while maska>0:
                wartosc=(l_copy%10)*(10**p) + wartosc
                if maska%10==1:

                    if not czy_pierwsza(wartosc):
                        break
                    p=0
                    wartosc=0
                else:
                    p+=1
                l_copy//=10
                maska//=10
            else:
                return True
    return False

print(divide(2347))