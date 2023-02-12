import math
def czy_mozna(w,pole):
    if pole < 10:
        return (w%10<pole)
    else:
        if w%10 < pole//10**(int(math.log10(pole))):
            return True
    return False

def rek(T,w=0,k=0):
    if w==len(T)-1 and k==len(T)-1:
        return True
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

T=[[15,16,13,],
    [85,72,13],
    [14,31,21]]


print(rek(T))

'''
if w==len(T)-1 and k==len(T)-1:
        return True
    if w<len(T)-1:
        if czy_mozna(T[w][k],T[w+1][k]):
            rek(T,w+1,k)
    if k<len(T)-1:
        if czy_mozna(T[w][k],T[w][k+1]):
            rek(T,w,k+1)
    if k<len(T)-1 and w<len(T)-1:
        if czy_mozna(T[w][k],T[w+1][k+1]):
            rek(T,w+1,k+1)
    return False
'''