import math
def czy_pierwsza(liczba):
    if liczba==2 or liczba==3:
        return True
    if liczba%2==0 or liczba%3==0 or liczba<2:
        return False
    i=5
    while i<math.sqrt(liczba)+1:
        if liczba%i==0:
            return False
        i+=2
        if liczba%i==0:
            return False
        i+=4
    return True

def iloczyn(liczba):
    i=2
    while i<=math.sqrt(liczba):
        if liczba%i==0:
            if czy_pierwsza(i) and czy_pierwsza(liczba//i):
                return True
        i+=1
    return False

def fun(t1,t2):

    for dl in range(1,len(t1)): # dl pierwszej tablicy
        suma=0
        for ix1 in range(len(t1)-dl+1): #indeks startowy w t1
            for i in range(dl):#suma w t1
                suma+=t1[ix1]
            
            for ix2 in range(len(t2)-dl+1): #indeks startowy w t2
                suma_copy=suma
                for i in range(dl): #suma w t2
                    suma_copy+=t2[ix2]

                if iloczyn(suma_copy):
                    print(dl)
                    print(suma_copy)
                    return True
    return False

t1=[6,6,5]
t2=[7,4,6]
print(fun(t1,t2))