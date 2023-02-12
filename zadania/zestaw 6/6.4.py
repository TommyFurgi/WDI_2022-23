def skoczek(T,w=0,k=0,n=1):
    T[w][k]=n
    if n==len(T)**2:
        return True

    for x,y in [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]:
         if warunek(T,w+x,k+y) and T[w+x][k+y]==0:
            if skoczek(T,w+x,k+y,n+1):
                return True
    T[w][k]=0
    return False

def warunek(T,w,k):
    if 0<= w <len(T) and 0<= k <len(T):
        return True
    return False

T=[[0 for _ in range(5)] for _ in range(5)]
skoczek(T)
for i in T:
    print(i)

'''
na zajeciach

def czy_mozna(T,w,k):
    if 0<=k<=7 and 0<=w<=7 and T[w][k]==0:
        return True
    retunrn False

def skoczek(T,w=0,k=0,n=1):
    T[w][k]=n
    if n==len(T)**2:
        print(T)
        return True

    skoki=[(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
    for skok in skoki:
        next_w=skok[0]+w
        next_k=skok[1]+k
        if czy_mozna(T,w_next,k_next):
            if skoczek(T,w_next,k_next,n+1)
                return True
    T[w][k]=0
    return False

'''
    