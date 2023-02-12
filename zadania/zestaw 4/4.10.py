def fun(tab):
    for i in tab:
        flaga=0
        for j in i:
            if j==0:
                flaga=1
                break
        if flaga==0:
            return False

    n=len(tab)
    i=0
    while i<n:
        j=0
        flaga=0
        while j<n:
            if tab[j][i]==0:
                flaga=1
                break
            j+=1
        if flaga==0:
            return False
        i+=1
    return True

tab = [
    [1,0,0,0,1,1,1,0],
    [1,0,1,0,1,1,1,0],
    [0,0,0,0,1,1,1,0],
    [0,0,0,0,1,0,1,0],
    [1,0,0,0,1,1,1,1],
    [1,1,0,1,1,0,1,0],
    [1,0,0,0,0,0,1,0],
    [1,1,1,0,1,1,1,1]
]
print(fun(tab))