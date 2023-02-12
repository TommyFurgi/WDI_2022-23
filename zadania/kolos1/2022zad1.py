def sequence(T):
    n=len(T)
    t=[[0 for _ in range(2)] for i in range(n)]
    i=0
    dl=0
    indeks=0
    while i<n:
        if dl==0:
            dl+=1
        if T[i-1]<T[i]:
            dl+=1
        elif dl>=3:
            t[indeks][0]=T[i-dl]
            t[indeks][1]=T[i-1]
            indeks+=1
            dl=0
        else:
            dl=0
        i+=1

    i=0
    while t[i][0]!=0:
        j=0
        while t[j][1]!=0:
            if t[i][0]>t[j][1]:
                return True
            j+=1
        i+=1
    return False
            
tab=[2,15,17,13,17,19,23,2,6,4,8,3,5,7,1,3,2]
print(sequence(tab))