def czy_mozna(T,w,k):
    for i in range(len(T)):
        if T[i][k]!=0 and T[w][i]!=0:
            return False

        if 0<=(i+w)<8 and 0<=(i+k)<8:
            if T[w+i][k+i]!=0:
                return False
        if 0<=w-i<8 and 0<=i+k<8:
            if T[w-i][k+i]!=0:
                return False
        if 0<=w-i<8 and 0<=k-i<8:
            if T[w-i][k-i]!=0:
                return False
        if 0<=i+w<8 and 0<=k-1<8:
            if T[w+i][k-i]!=0:
                return False
    return True


def zad(T,w=0,k=0,n=1):
    T[w][k]=1
    if n==len(T):
        return True
    for i in range(len(T)):
        if czy_mozna(T,w+1,i):
            if zad(T,w+1,i,n+1):
                return True
    T[w][k]=0
    return False

T=[[0 for _ in range(8)] for _ in range(8)]
zad(T)
for i in T:
    print(i)