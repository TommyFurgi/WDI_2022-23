def system(liczba):
    wynik=0
    i=0
    while liczba>0:
        wynik=(liczba%4)*10**i+wynik
        liczba//=4
        i+=1
    return wynik

def cyfry(liczba):
    tab=[False]*10
    while liczba>0:
        tab[liczba%10]=True
        liczba//=10
    return tab
def czy_te_same_cyfry(t1,t2):
    i=0
    while i<10:
        if t1[i]!=t2[i]:
            return False
        i+=1
    return True
def fun(T):
    n=len(T)
    naj=0
    licznik=1
    t1=[False]*10
    for i in range(n):
        t1=cyfry(system(T[i]))
        for j in range(i+1,n): 
            t2=cyfry(system(T[j]))
            if czy_te_same_cyfry(t1,t2):
                licznik+=1


        naj=max(naj,licznik)
        licznik=1
    return naj


tab=[18,13,36,74,99]
print(fun(tab))