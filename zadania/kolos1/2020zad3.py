def suma(w1,k1,w2,k2,T):
    sum=0
    n=len(T)
    if w1==w2:
        for i in range(n):
            sum+=T[i][k1]
            sum+=T[i][k2]
            sum+=T[w1][i]
        sum-=T[w1][k1]
        sum-=T[w2][k2]

    elif k1==k2:
        for i in range(n):
            sum+=T[i][k1]
            sum+=T[w1][i]
            sum+=T[w2][i]
        sum-=T[w1][k1]
        sum-=T[w2][k2]
    else:
        for i in range(n):
            sum+=T[w1][i]
            sum+=T[w2][i]
            sum+=T[i][k2]
            sum+=T[i][k1]
        sum-=T[w1][k2]
        sum-=T[w2][k1]
        sum-=T[w1][k1]
        sum-=T[w2][k2]
    return sum-T[w1][k1]-T[w2][k2]
       

def chess(T):
    n=len(T)
    x1=0
    x2=0
    y1=0
    y2=0
    naj=0
    for w1 in range(n):
        for k1 in range(n):
            for w2 in range(n):
                for k2 in range(n):
                    if w1==w2 and k1==k2:
                        continue
                    sum=suma(w1,k1,w2,k2,T)
                    if sum>naj:
                        naj=sum
                        x1=w1
                        x2=w2
                        y1=k1
                        y2=k2
    return (x1,y1,x2,y2),naj
print(chess([[4,0,2],[3,0,0],[6,5,3]]))