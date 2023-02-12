import math
def srodek_ciezkosci(T):
    y=0
    x=0
    for i,j in (T):
        y+=j
        x+=i
    return (x/len(T),y/len(T))

def rek(T,index=0,w1=[],w2=[]):
    if index==len(T):
        if len(w1)==0 or len(w2)==0 or w1==w2:
            return  float('inf')
        else:
            t1=srodek_ciezkosci(w1)
            t2=srodek_ciezkosci(w2)
            return math.sqrt((t1[1]-t2[1])**2+(t1[2]-t2[2]**2))

    return min(rek(T,index+1,w1+T[index],w2),rek(T,index+1,w1,w2+T[index]),rek(T,index+1,w1,w2))