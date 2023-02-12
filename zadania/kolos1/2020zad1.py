import math
def czy_wielokrotny(napis):
    dl=len(napis)
    i=int(math.sqrt(dl))+1
    while i>=1:
        if dl%i==0:
            nap=napis[0:i]*(dl//i)
            if nap==napis:
                return dl
        i-=1
    return 0

def multi(T):
    naj=0
    for i in T:
        naj=max(czy_wielokrotny(i),naj)
    return naj

T=["ABCABCABC","DFGHJ","POPOPOPOPOPO"]
print(multi(T))