def rek(t,n=1,x=0,y=0):
    t[x][y]=n
    if n==len(t)**2:
        for i in t:
            print(i)
        return True

    for i,j in [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]:
        if 0<=i+x<len(t) and 0<=y+j<len(t):
            if t[x+i][y+j]==0:
                if rek(t,n+1,x+i,y+j):
                    return True
    t[x][y]=0
    return False

t=[[0 for _ in range(6)] for _ in range(6)]
rek(t)