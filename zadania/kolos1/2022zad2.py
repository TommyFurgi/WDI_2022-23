def czynniki(liczba):
    flaga1=False
    flaga2=False
    while liczba%2==0:
        flaga1=True
        liczba//=2

    i=3
    while liczba!=1:
        if liczba%i==0:
            if flaga1==True:
                flaga2=True
            else:
                flaga1=True
            liczba//=i
            while liczba%i==0:
                liczba//=i
        if flaga2==True:
            if liczba!=1:
                return False
            else:
                return True
        i+=1

def square(T):

    n=len(T)
    for bok in range(3,n):
        for i in range(n-bok+1):
            for j in range(n-bok+1):
                iloczyn=T[i][j]*T[i+bok-1][j]*T[i][j+bok-1]*T[i+bok-1][j+bok-1]
                if czynniki(iloczyn):
                    return bok
    return 0

t = [[2,22,4,7],
    [585,35,438,31],
    [9,8,6,88],
    [5,15,8,8]] 
print(square(t))