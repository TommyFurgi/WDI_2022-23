def A(liczba):
    return liczba+2
def B(liczba):
    return liczba*2
def C(liczba):
    wynik=0
    p=0
    while liczba>0:
        if liczba%2==0:
            wynik=((liczba%10)+1)*10**p+wynik
        else:
            wynik=((liczba%10))*10**p+wynik
        liczba//=10
        p+=1
    return wynik
    
def mask(liczba):
    wynik=0
    p=0
    while liczba>0:
        wynik=(liczba%4)*10**p+wynik
        liczba//=4
        p+=1
    return wynik

def czy_podwojjne(maska):
    last=5
    while maska>0:
        if maska%10==last:
            return False
        last=maska%10
        maska//=10
    return True
        

def f(x,y,n):
    suma=0
    for i in range(4**n):
        maska = mask(1)
        if not czy_podwojjne:
            continue
        x_copy=x
        while maska>0:
            if maska%10==1:
                x_copy=A(x_copy)
            if maska%10==2:
                x_copy=B(x_copy)
            if maska%10==3:
                x_copy=C(x_copy)
            maska//=10
        if x_copy==y:
            suma+=1
    return suma
