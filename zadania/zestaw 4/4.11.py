def sortuj(liczba):
    wynik=0
    t=[False]*10
    while liczba>0:
        t[liczba%10]=True
        liczba//=10
    i=1
    while i<len(t):
        if t[i]==True:
            wynik=wynik*10+i
        i+=1
    if t[0]==True:
        wynik*=10
    return wynik


def fun(tab):
    i=0
    n=len(tab)
    t=[[0 for _ in range(n)]for _ in range(n)]
    while i<len(tab):
        j=0
        while j<len(tab):
            t[i][j]=sortuj(tab[i][j])
            j+=1
        i+=1


    licznik=0
    i=1
    while i<len(tab):
        j=1
        while j<len(tab):
            if j+1<len(tab):
                if t[i][j]!=t[i][j+1]:
                    j+=1
                    continue
            if j-1>-1:
                if t[i][j]!=t[i][j-1]:
                    j+=1
                    continue
            if i+1<len(tab):
                if t[i][j]!=t[i+1][j]:
                    j+=1
                    continue
            if i-1>-1:
                if t[i][j]!=t[i-1][j]:
                    j+=1
                    continue

            licznik+=1
            print(i,j)
            j+=1
        i+=1
    return licznik

tab = [
    [1,0,0,0,1,1,1,0],
    [1,0,1,0,1,1,1,0],
    [0,0,0,0,1,1,1,0],
    [0,0,0,0,1,0,1,0],
    [1,0,0,0,1,1,1,1],
    [1,1,0,1,1,0,1,0],
    [1,0,0,0,0,0,1,0],
    [1,1,1,0,1,1,1,1]
]
print(fun(tab))


'''
licznik=0
    i=1
    while i<len(tab)-1:
        j=1
        while j<len(tab)-1:
            
            if tab[i][j]==tab[i][j+1] and tab[i][j]==tab[i+1][j] and tab[i][j]==tab[i-1][j] and tab[i][j]==tab[i][j-1]: #to działa tylko dla kwadracika w srodku
                licznik+=1
                print(i,j)
            j+=1
        i+=1
    return licznik
'''