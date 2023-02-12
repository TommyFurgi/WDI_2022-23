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


def unikalne_cyfry(liczba):
    tab=[False]*10
    while liczba>0:
        if tab[liczba%10]==True:
            return False
        else:
            tab[liczba%10]=True
        liczba//=10
    return True

def fun(liczba):
    dl=int(math.log10(liczba))+1

    M=0
    max_=0
    while liczba>0:
        l_copy=liczba
        while l_copy>0:
            if unikalne_cyfry(l_copy) and czy_pierwsza(l_copy):
                if l_copy>max_:
                    max_=l_copy
            l_copy//=10
        M+=1
        liczba=liczba%(10**(dl-M))
    return max_

print(fun(1202742516))

'''
import math
def cyfry(l):
    t=[False]*10
    while l>0:
        if t[l%10]==True:
            return False
        t[l%10]=True
        l//=10
    return True
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
def d(l):
    licznik=0
    while l>0:
        licznik+=1
        l//=10
    return licznik
def fun(K):
    n=d(K)  
    najw=0
    for dl in range(1,n):
        k_copy=K
        for i in range(n-dl+1):
            wartosc//=10**(n-dl-i)
            wartosc=k_copy%10**(dl)
            if czy_pierwsza(wartosc) and cyfry(wartosc):
                najw=max(najw,wartosc)
    return najw

print(fun(1202742516))
'''