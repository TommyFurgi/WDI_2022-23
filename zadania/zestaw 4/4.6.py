def sortuj(t):
    n=len(t)
    for i in range(n):
        for j in range(n-1):
            if t[j]==0:
                t[j],t[j+1]=t[j+1],t[j]
            elif t[j]>t[j+1] and t[j+1]!=0:
                t[j],t[j+1]=t[j+1],t[j]

def fun(t1):
    t2=[0 for _ in range(len(t1)**2)]
    n=len(t1)


    indeks=0
    for i in t1:
        for j in i:
            t2[indeks]=j
            indeks+=1
    sortuj(t2)
    i=0
    while i<len(t2)-1:
        if t2[i]==t2[i+1]:
            wartosc=t2[i]
            t2[i]=0
            t2[i+1]=0
            i+=2
            if i==len(t2)-1 and t2[i]==wartosc:
                t2[i]=0
                break
            while t2[i]==wartosc:
                t2[i]=0
                i+=1
                if i==len(t2)-1:
                    break
        i+=1
    print(t2)
    sortuj(t2)
    return t2


t1=[[1,2,9],[4,6,11],[3,11,12]]
print(fun(t1))

'''
    for i in t1:
        indeks=0
        for j in i:
            while True:
                if j==t2[indeks]:
                    p=indeks
                    while t2[p]!=0:
                        t2[p]=t2[p+1]
                        p+=1
                    break
                elif j<t2[indeks] or t2[indeks]==0:
                    p=indeks
                    temp=j
                    while temp!=0:
                        temp, t2[p]=t2[p], temp
                        p+=1
                    break
                elif j>t2[indeks]:
                    indeks+=1 
        indeks+=1
'''