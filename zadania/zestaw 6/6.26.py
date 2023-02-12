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
def sys(liczba):
    wynik=0
    i=0
    while liczba>0:
        if liczba%10==1:
            wynik+=2**i
        i+=1
        liczba//=10
    return wynik
def fun(A,B):
    licznik=0
    def rek(A,B,wynik=0):
        if A==0 and B==0:
            nonlocal licznik
            if not czy_pierwsza(sys(wynik)):
                licznik+=1
            return 

        if A>0:
            rek(A-1,B,1+wynik*10)
        if B>0 and wynik!=0:
            rek(A,B-1,wynik*10)
    rek(A,B)
    return licznik

print(fun(3,2))
