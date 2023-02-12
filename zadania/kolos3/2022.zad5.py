'''Dwie liczby naturalne są czynnikowo-podobne, jeżeli w swoich rozkładach na czynniki pierwsze mają
dokładnie jeden czynnik równy. Na przykład: 24 i 14 albo 32 i 18. Dana jest tablica T[N ][N ]
zawierająca liczby naturalne. Dwie liczby sąsiadują ze sobą wtedy, gdy leżą w sąsiednich kolumach i
sąsiednich wiersza. Proszę napisać funkcję three(T), która zwraca ilość liczb w tablicy sąsiadujących
dokładnie z 3 liczbami czynnikowo-podobnymi.'''

def czynniki(a,b):
    flag1=False
    i=2
    while i<=a and i<=b:
        if a%i==0 and b%i==0:
            if flag1==False:
                flag1=True
            else:
                return False
            while a%i==0:
                a//=i
            while b%i==0:
                b//=i
        i+=1

    return flag1

def tree(T):
    n=len(T)
    cnt=0
    for i in range(1,n-1):
        for j in range(1,n-1):
            k=0
            for x,y in [(1,1),(-1,1),(1,-1),(-1,-1)]:
                if czynniki(T[i][j],T[i+x][j+y]):
                    k+=1
            if k==3:
                cnt+=1
    return cnt