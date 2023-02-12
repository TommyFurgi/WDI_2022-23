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

def fun(tab):
    i=0
    a,b=1,1
    flaga=0
    while i<len(tab):
        if i==b:
            a,b=b,a+b
            if czy_pierwsza(tab[i]) or tab[i]==0 or tab[i]==1:
                return False
        else:
            if flaga==0 and czy_pierwsza(tab[i]):
                flaga=1
        i+=1

    if flaga==1:
        return True
    else:
        return False

t=[2,8,32,33,45,45,19,17,68]
print(fun(t))