import math
def dlugosc(liczba):
    licznik=0
    while liczba>0:
        licznik+=1
        liczba//=10
    return licznik

def fun(a,b,mask):
    wynik=0
    i=0
    while mask>0 or b>0:
        if mask%2==1:
            wynik=a%10*10**i+wynik
            a//=10
        else:
            wynik=b%10*10**i+wynik
            b//=10
        i+=1
        mask//=10
    return wynik

def is_prime(liczba):
    if liczba==2 or liczba==3:
        return True
    elif liczba<2 or liczba%2==0 or liczba%3==0:
        return False
    i=5
    while i<int(math.sqrt(liczba))+1:
        if liczba%i==0:
            return False
        i+=2
        if liczba%i==0:
            return False
        i+=4
    return True

def binarny(liczba):
    wynik=0
    i=0
    while liczba>0:
        wynik=liczba%2*10**i+wynik
        liczba//=2
        i+=1
    return wynik

def czy_dobra_maska(a,b,mask):
    cnt1=dlugosc(a)
    cnt2=dlugosc(b)
    while mask>0:
        if mask%2==0:
            cnt2-=1
        else:
            cnt1-=1
        mask//=10
    return cnt1==0 and cnt2>=0

def koncowa(a,b):
    i=0
    licznik=0
    suma_dlugosci=dlugosc(a)+dlugosc(b)
    for i in range(2**(suma_dlugosci)):
        mask=binarny(i)
        if czy_dobra_maska(a,b,mask) and is_prime(fun(a,b,mask)):
            licznik+=1
    return licznik
print(koncowa(123,75))
    