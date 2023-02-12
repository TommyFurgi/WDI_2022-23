def move(T):
    w=[0]*len(T)
    k=[0]*len(T)
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j]==True:
                w[i]+=1
                k[j]+=1

    for i in range(len(T)):
        for j in range(len(T)):
            if w[i]>=2 and k[j]>=2:
                a,b=i,j
                break

    for i in range(len(T)):
        for j in range(len(T)):
            if w[i]==0 and k[j]==0:
                return (a,b),(i,j)
