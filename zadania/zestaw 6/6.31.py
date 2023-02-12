def podzielniki(n):
    w=[1]*20
    i=2
    j=0
    while n!=1:
        if n%i==0:
            w[j]=i
            j+=1
            while n%i==0:
                n//=i
        i+=1
    return w

def fun(liczba):
    suma=0
    w=podzielniki(liczba)
    def rek(w,pos=0,wynik=1):
        if w[pos]==1:
            nonlocal suma
            if wynik!=1:
                suma+=wynik
            return
        rek(w,pos+1,wynik*w[pos])
        rek(w,pos+1,wynik)

    rek(w)
    return suma
print(podzielniki(60))
print(fun(60))