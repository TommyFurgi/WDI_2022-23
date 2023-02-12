def fun(T,w,k):
    if w==7:
        return T[w][k]
    if k>0:
        lewy=fun(T,w+1,k-1)
    else:
        lewy=float('inf') # oznacza nieskonczonosc

    if k<7:
        prawy=fun(T,w+1,k+1)
    else:
        prawy=float('inf') # oznacza nieskonczonosc

    srodek=fun(T,w+1,k)

    return T[w][k] + min(lewy,prawy,srodek)
