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


def fun(a,b):
    licz=0
    def rek(a,b,wynik=0,pos=0):
        if a==0 and b==0:
            if czy_pierwsza(wynik):
                nonlocal licz
                print(wynik)
                licz+=1
        if a!=0:
            rek(a//10,b,(a%10)*10**pos+wynik,pos+1)
        if b!=0:
            rek(a,b//10,(b%10)*10**pos+wynik,pos+1)
        
    rek(a,b)
    return licz

print(fun(123,75))
