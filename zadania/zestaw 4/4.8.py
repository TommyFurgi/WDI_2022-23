def fun(t):
    dl=0
    najdluzszy=0
    i=0
    n=len(t)
    while i<n-2:
        j=0
        while j<n-2:
            q=0
            p=0
            while True:
                if q==0:
                    q=t[i+1][j+1]//t[i][j]
                    dl+=1
                if i+p+1<n: 
                    if t[i+1+p][j+1+p]//t[i+p][j+p]==q:
                        dl+=1
                        p+=1
                    else:
                        najdluzszy=max(najdluzszy,dl)
                        dl=0
                        break
                else:
                    najdluzszy=max(najdluzszy,dl)
                    dl=0
                    break
            j+=1
        i+=1
    if najdluzszy>=3:
        return najdluzszy
    else:
        return None




t = [[2,2,1,7],
    [7,4,1,8],
    [12,8,8,88],
    [4,15,16,16]] 
print(fun(t))