def jedynki(liczba):
    ilosc=0
    while liczba>0:
        if liczba%2==1:
            ilosc+=1
        liczba//=2
    if ilosc%2==0:
        return False
    else:
        return True
    
def fun(tab):
    flaga=0
    n=len(tab)
    i=0
    t=[[jedynki(tab[i][j]) for j in range(n)] for i in range(n)]
    for w in range(n):
        for k1 in range(n):
            for k2 in range(n):
                if k1!=k2:
                    licznik=0
                    for i in range(n):
                        for j in range(n):
                            if i!=w and k1!=j and k2!=j:
                                if t[i][j]==True:
                                    licznik+=1
                    if licznik==n*n-3*n+2:
                        return True
    return False
t=[[4,4,5,5],
    [5,5,5,5],
    [4,4,5,5],
    [4,4,5,5]]
print(fun(t))