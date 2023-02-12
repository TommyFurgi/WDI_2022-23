import math
def srodek_ciezkosci(tab):
    a,b,c=0,0,0
    for x,y,z in tab:
        a+=x
        b+=y
        c+=z
    return (x,y,z)

def rek(T,r,pos=0,w=[]):
    if len(w)==3:
        x,y,z=srodek_ciezkosci(w)
        if math.sqrt(z**2+x**2+y**2)<=r:
            return True
        return False
    if pos==len(T):
        return False

    return rek(T,r,pos+1,w) or rek(T,r,pos+1,w+[T[pos]])

arr = [
    (4,1,2), 
    (4,6,1),
    (1,8,8), 
    (4,8,8),
    (4,8,2), 
    (1,1,1)
]

print(rek(arr,5))