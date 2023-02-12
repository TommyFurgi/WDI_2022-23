import math
def A(n):
    n_copy=n
    dl=int(math.log10(n))
    ost=n%10
    pier=n_copy//(10**dl)
    reszta=n%(10**dl)
    reszta//=10
    return ost*10**dl+reszta*10+pier

def B(n):
    return n*3


def C(n):
    dl=int(math.log10(n))
    return n%(10**dl)

def fun(x,y):
    nap=""
    def rek(x,y,napis="",n=0):
        if n==8:
            return False
        if x==y:
            nonlocal nap
            nap=napis
            return True

        for i in range(3):
            if (i==0 or i==2) and int(math.log10(x))>0:
                if i==0:
                    if rek(A(x),y,napis+"A",n+1):
                        return True
                if i==2:
                    if rek(C(x),y,napis+"C",n+1):
                        return 
            if rek(B(x),y,napis+"B",n+1):
                        return True
        return False
    rek(x,y)
    return nap

print(fun(6,3))