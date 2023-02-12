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

def fun(tab):
    n=len(tab)
    t=[[False for _ in range(n) ] for _ in range(n)]

    i=0
    while i<n: #iteujemy po kolejnych polach w liscie
        j=0
        while j<n:
            l=0
            while l<n: # szukamy liczbe komplementarna
                k=0
                while k<n:
                    if not (i==l and j==k):
                        if czy_pierwsza(tab[i][j]+tab[l][k]):
                            t[i][j]=True
                            t[l][k]=True
                            print(tab[i][j],tab[l][k])
                            break
                    k+=1
                l+=1
            j+=1
        i+=1
    i=0
    while i<n:
        j=0
        while j<n:
            if t[i][j]==False:
                tab[i][j]=0
            j+=1
        i+=1
    return tab

t = [[2,2,1,7],
    [7,5,1,9],
    [9,8,7,88],
    [5,15,8,8]] 
t=fun(t)
for i in t:
    print(i)