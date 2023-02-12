def suma(x1,y1,x2,y2,t):
    s=0
    n=len(t)
    for i in range(n):
        if x1==x2:
            s+=t[x1][i]
            s+=t[i][y1]
            s+=t[i][y2]
        elif y1==y2:
            s+=t[x1][i]
            s+=t[i][y1]
            s+=t[x2][i]
        else:
            s+=t[x1][i]
            s+=t[i][y1]
            s+=t[x2][i]
            s+=t[i][y2]
    s-=t[x1][y1]
    s-=t[x2][y2]
    s-=t[x1][y2]
    s-=t[x2][y1]
    return s