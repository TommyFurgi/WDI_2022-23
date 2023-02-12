def czy_nalezy(x,y,t):
    for a,b in t:
        if a==x and y==b:
            return True
    return False


def rook(N,L):
    def rek(N,t,x=0,y=0,ile=0,last=""):
        if x==N-1 and y==N-1:
            return ile
        if x==N or y==N or czy_nalezy(x,y,t):
            return float('inf')

        if last=="dol":
            return min(rek(N,t,x,y+1,ile+1,"prawo"),min(rek(N,t,x+1,y,ile,"dol")))
        elif last=="prawo":
            return min(rek(N,t,x,y+1,ile,"prawo"),min(rek(N,t,x+1,y,ile+1,"dol")))
        else:
            return min(rek(N,t,x,y+1,ile+1,"prawo"),min(rek(N,t,x+1,y,ile+1,"dol")))
    
    a=rek(N,L)
    if a=='inf':
        return None
    return a
    