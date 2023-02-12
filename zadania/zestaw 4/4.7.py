def fun(t1):
    t2=[0 for _ in range(len(t1)**2)]
    n=len(t2)
    for i in t1:
        indeks=n-1
        for j in i:
            while True:
                if j<t2[indeks] and t2[indeks]!=0:
                    indeks-=1
                else:
                    p=indeks
                    temp=j
                    while temp!=0:
                        temp,t2[p]=t2[p],temp
                        p-=1
                    break


    return t2

t1=[[2,2,1],[7,5,1],[12,11,11]]
print(fun(t1))