def fun(t):
    n=len(t)
    suma=0
    suma_najw=0
    i=0
    ix=0
    iy=0
    while i<n:
        j=0
        while j<n: #czy da sie efektywniej? da
            suma=0
            if i-1>0:
                suma+=t[i-1][j]
            if j-1>0:
                suma+=t[i][j-1]
            if i+1<n:
                suma+=t[i+1][j]
            if j+1<n:
                suma+=t[i][j+1]

            if i-1>0 and j-1>0:
                suma+=t[i-1][j-1]
            if j-1>0 and i+1<n:
                suma+=t[i+1][j-1]
            if i+1<n and j+1<n:
                suma+=t[i+1][j+1]
            if j+1<n and i-1>0: 
                suma+=t[i-1][j+1]

            if suma>suma_najw:
                ix=i
                iy=j
                suma_najw=suma
            j+=1
        i+=1
    print(suma_najw)
    return ix,iy

t = [[2,22,1,7],
    [585,35,2,31],
    [9,8,7,88],
    [5,15,8,8]] 
print(fun(t))