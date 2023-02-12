def fun(tab,k):
    n=len(tab)
    i=0

    while i<n:
        j=0
        while j<n:
            bok=3
            while i+bok<n and j+bok<n:
                suma=0
                suma+=tab[i][j]
                suma+=tab[i][j+bok-1]
                suma+=tab[i+bok-1][j]
                suma+=tab[i+bok-1][j+bok-1]
                if suma==k:
                    return i+bok//2, j+bok//2
                bok+=2
            j+=2
        i+=1
    return None

T = [
    [1,0,0,0,1,1,1,0],
    [1,0,1,0,1,1,1,0],
    [0,0,13,0,1,1,1,0],
    [0,0,0,0,1,0,1,0],
    [1,0,0,0,1,1,1,1],
    [1,1,0,1,1,9,1,0],
    [1,0,0,0,0,0,1,0],
    [1,1,1,0,1,1,1,1]
]
print(fun(T,4))