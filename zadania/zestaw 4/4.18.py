def fun(T):
    n=len(T)
    suma=0
    res=0
    for x in range(n):
        for y in range(n):
            for dl in range(1,11):
                if dl+x<=n:
                    for i in range(x,x+dl):
                        suma+=T[i][y]
                    res=max(res,suma)
                    suma=0
                if dl+y<=n:
                    for i in range(y,y+dl):
                        suma+=T[x][i]
                    res=max(res,suma)
                    suma=0
    return res

t = [[2,22,1,7],
    [585,35,2,31],
    [9,8,7,88],
    [5,15,8,8]] 
print(fun(t))