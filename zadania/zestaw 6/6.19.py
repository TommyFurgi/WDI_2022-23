import math
def czy_mozna(w,pole):
    if pole < 10:
        return (w%10<pole)
    else:
        if w%10 < pole//10**(int(math.log10(pole))):
            return True
    return False

def czy_nalezy(W,krotka):
    for x in W:
        if x==krotka:
            return True
    return False


def rek(T,w=0,k=0,W=[]):
    if (w==len(T)-1 and k==len(T)-1) or (w==0 and k==0) or (w==len(T)-1 and k==0) or (w==0 and k==len(T)-1):
        print(w,k)
        return True
    for x,y in [(1,1),(1,0),(1,-1),(-1,0),(-1,1),(-1,-1),(0,1),(0,-1)]:
        if 0<=x+w<len(T) and 0<=k+y<len(T):
            if czy_mozna(T[w][k],T[x+w][k+y]):
                if not czy_nalezy(W,(w+x,k+y)):
                    if rek(T,w+x,k+y,W+[(w+x,k+y)]):
                        
                        return True
    W=W[:-1]
    return False
    

   

T=[
    [1,4,6,2,3,5,35,2],
    [1,4,6,2,3,5,35,2],
    [1,4,6,82,3,5,35,2],
    [1,4,6,2,3,5,35,2],
    [1,4,6,2,3,5,91,2],
    [1,4,6,82,3,5,24,2],
    [1,4,6,2,3,5,35,7],
    [1,4,6,2,3,5,35,8],
]

print(rek(T,1,1))

'''
 if w<len(T)-1:
        if czy_mozna(T[w][k],T[w+1][k]):
            if rek(T,w+1,k):
                return True
    if k<len(T)-1:
        if czy_mozna(T[w][k],T[w][k+1]):
            if rek(T,w,k+1):
                return True
    if k<len(T)-1 and w<len(T)-1:
        if czy_mozna(T[w][k],T[w+1][k+1]):
            if rek(T,w+1,k+1):
                return True   
    return False   
'''