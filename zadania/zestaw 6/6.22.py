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

def zad(t):
    i=-1
    def rek(t,indeks=0,skoki=0):
        if indeks>=len(t):
            return False
        if indeks==len(t)-1:
            nonlocal i
            i=skoki
            return True

        for k in range(1,len(t)):
            if k<t[indeks] and t[indeks]%k==0 and czy_pierwsza(k):
                if rek(t,indeks+k,skoki+1):
                    return True
        return False

    rek(t)
    return i

t=[12,5,1,6,1,3]
print(zad(t))