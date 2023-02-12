import math
def dl(liczba):
    licznik=0
    while liczba>0:
        licznik+=1
        liczba//=10
    return licznik

def fun(liczba,mask):
    wynik=0
    i=0
    while mask>0:
        if mask%2==1:
            wynik=liczba%10* 10**i+wynik
            i+=1
        mask//=10
        liczba//=10
        
    return wynik

def binarny(liczba):
    wynik=0
    i=0
    while liczba>0:
        wynik=liczba%2*10**i+wynik
        liczba//=2
        i+=1
    return wynik

liczba=int(input())
dlugosc=dl(liczba)
licznik=0


for i in range (1,2**dlugosc):
    mask = binarny(i)
    if fun(liczba, mask)%7==0:
        licznik+=1

print(licznik)