def fun(t):
    ix=0
    suma=0
    dl=0
    najw=0
    n=len(t)
    for i in range(n-1):
        if dl==0:
            dl+=1
            suma+=t[i]
            ix+=1
        if t[i]<t[i+1]:
            dl+=1
            suma+=t[i+1]
            ix+=(i+1)
            if suma==ix:
                najw=max(dl,najw)
        else:
            dl=0
            ix=0
            suma=0
    return najw

t=[4,1,2,3,7]
print(fun(t))