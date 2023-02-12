def cyfry(a,b):
    t=[False]*10
    while a>0:
        t[a%10]=True
        a//=10
    flag=False
    while b>0:
        if t[b%10]==True:
            if flag==True:
                return True
            flag=True
        b//=10
    return False

def zad(T):
    n=len(T)
    cnt=n**2
    for i in range(n):
        for j in range(n):
            flag=False
            k=T[i][j]
            if k<10:
                T[i][j]=0
                cnt-=1
            for x in range(n):
                for y in range(n):
                    if x!=i and y!=j and flag==False:
                        l=T[x][y]
                        if cyfry(k,l):
                            flag=True
                            break
            if flag==False:
                T[i][j]=0
                cnt-=1
    return cnt