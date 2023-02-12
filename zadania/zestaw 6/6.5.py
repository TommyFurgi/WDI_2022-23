import math
def sys(l):
    p=0
    wynik=0
    while l>0:
        wynik+=(l%10)*2**p
        l//=10
        p+=1
    return wynik

def is_prime(l):
    if l==2 or l==3:
        return True
    if l%2==0 or l%3==0 or l<2:
        return False
    i=5
    while i<math.sqrt(l)+1:
        if l%i==0:
            return False
        i+=2
        if l%i==0:
            return False
        i+=4
    return True

def fun(T,wynik=0,pos=0,dl=0,b=False):
    if pos==len(T):
        if (is_prime(sys(wynik)) and dl<=30):
            return True
        else:
            return False
    if b==True:
        if not (is_prime(sys(wynik)) or dl<=30):
            return False
        wynik=0
        dl=0
        b=False
    return fun(T,wynik*10**dl+T[pos],pos+1,dl+1,b=True) or fun(T,wynik*10**dl+T[pos],pos+1,dl+1,b)

T=[1,1,1,0,1,1]
print(fun(T))
