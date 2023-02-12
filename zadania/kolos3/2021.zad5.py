def nwd(a,b):
    while b:
        a,b=b,a%b
    return a

def trojki(T,n=0,ile=0,P=[],flag=False):
    if ile==3:
        if nwd(P[0],P[1])==1 and nwd(P[0],P[2])==1 and nwd(P[1],P[2])==1:
            print(P)
            return 1
        return 0

    if n==len(T):
        return 0

    if flag==True and ile!=0:
        return trojki(T,n+1,ile+1,P+[T[n]],flag=False)
    return trojki(T,n+1,ile+1,P+[T[n]],flag=False) + trojki(T,n+1,ile,P,flag=True)


print(trojki([2,3,4,5,6,8,7]))