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


def rek(n,a=0,pos=0,ile=0):
    if n<=0:
        if czy_pierwsza(ile+1) and czy_pierwsza(a):
            return True
        return False

    if czy_pierwsza(a):
        return rek(n//10,a+(n%10)*10**pos,pos+1,ile) or rek(n//10,n%10,1,ile+1)
    return rek(n//10,a+(n%10)*10**pos,pos+1,ile)


print(rek(23672))