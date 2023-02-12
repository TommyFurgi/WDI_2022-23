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

'''ruchy
0 1 2
7 X 3
6 5 4
'''
def zadanie(T,w,k):
    tab=[]
    def rek(T,w=0,k=0,W=[],ruchy=[]):
        if (w==len(T)-1 and k==len(T)-1) or (w==0 and k==0) or (w==len(T)-1 and k==0) or (w==0 and k==len(T)-1):
            nonlocal tab
            tab=ruchy
            return True

        for x,y,kierunki in [(1,1,4),(1,0,5),(1,-1,6),(-1,0,1),(-1,1,2),(-1,-1,0),(0,1,3),(0,-1,7)]:
            if 0<=x+w<len(T) and 0<=k+y<len(T):
                if czy_mozna(T[w][k],T[x+w][k+y]):
                    if not czy_nalezy(W,(w+x,k+y)):
                        if rek(T,w+x,k+y,W+[(w+x,k+y)],ruchy+[kierunki]):
                            return True
        W=W[:-1]
        return False
        
    if rek(T,w,k):
        return tab
    else:
        return None
   

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

print(zadanie(T,1,1))
