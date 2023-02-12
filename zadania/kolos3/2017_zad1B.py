'''Dwie liczby naturalne są „przyjaciółkami” jeżeli zbiory cyfr z których zbudowane są liczby
są identyczne. Na przykład: 123 i 321, 211 i 122, 35 i 3553. Dana jest tablica int t[N][N]
wypełniona liczbami naturalnymi. Proszę napisać funkcję, która dla tablicy t zwraca ile
elementów tablicy sąsiaduje wyłącznie z przyjaciółkami.'''

def przyjaciele(a,b):
    t1=[False]*10
    t2=[False]*10
    while a>0:
        t1[a%10]=True
        a//=10
    
    while b>0:
        t2[b%10]=True
        b//=10

    for i in range(10):
        if t1[i]!=t2[i]:
            return False
    return True

def zad(t):
    n=len(t)
    cnt=0
    for i in range(n):
        for j in range(n):
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                if 0<=i+x<n and 0<=j+y<n:
                    if not przyjaciele(t[i][j],t[i+x][j+y]):
                        break
            else:
                cnt+=1
    return cnt