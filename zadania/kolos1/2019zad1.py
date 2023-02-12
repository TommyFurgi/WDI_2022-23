import math
def suma_tab(tab,dl,indeks):
    suma=0
    for i in range(dl):
        suma+=tab[indeks+i]
    return suma

def jest_potega(liczba):
    i=2
    while i<math.sqrt(liczba):
        l_copy=liczba
        while True:
            if l_copy==1:
                return True
            if l_copy%i!=0:
                break
            else:
                l_copy//=i
        i+=1
    return False
            

def fun(t1,t2):
    n1=len(t1)
    n2=len(t2)
    for i in range(1,24):#dlugosc pierwszego wycinka
        for ix1 in range(n1-i+1): #poczatek 1 wycinka
            for ix2 in range(n2-24+i+1): #poczatek 2 wycinka
                suma = suma_tab(t1,i,ix1)+suma_tab(t2,24-i,ix2)
                if jest_potega(suma):
                    return True
    return False

t1=[i for i in range(100)]
t2=[i+5 for i in range(100)]

print(fun(t1,t2))