def ile_jedynek(liczba):
    licznik=0
    while liczba>0:
        if liczba%2==1:
            licznik+=1
        liczba//=2
    return licznik%2

def ile_w_tab(t):
    licznik=0
    for i in t:
        for j in i:
            if j==1:
                licznik+=1
    return licznik

def fun(t):
    t1=[[ile_jedynek(t[i][j] for i in range(len(t))) for j in range(len(t))]]
    for w in range(len(t)):
        for k1 in range(len(t)):
            for k2 in range(len(t)):
                if k1==k2:
                    continue
                tab=t1.copy
                for i in range(len(t)):
                    tab[w][i]=1
                    tab[i][k2]=1
                    tab[i][k1]=1
                if ile_w_tab(tab)==3*len(t)-2:
                    return True
    return False

