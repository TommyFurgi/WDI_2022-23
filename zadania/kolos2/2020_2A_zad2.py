import math
def A(n):
    return n+3

def B(n):
    return n*2

def C(n):
    p=0
    wynik=0
    for i in range(int(math.log10(n))+1):
        if n%2==0:
            wynik=wynik+((n%10)+1)*10**p
        else:
            wynik=wynik+(n%10)*10**p
        n//=10
        p+=1
        
    return wynik

def zad(x,y,N):
    licz=0
    w=[]
    def rek(x,y,N,pos=0,last="D",napis=""):
        if x==y:
            nonlocal licz
            licz+=1
            nonlocal w
            w=w+[napis]
            return
        if pos==N:
            return 
        if last!="A":
            rek(A(x),y,N,pos+1,"A",napis+"A")
        if last!="B":
            rek(B(x),y,N,pos+1,"B",napis+"B")
        if last!="C":
            rek(C(x),y,N,pos+1,"C",napis+"C")
    rek(x,y,N)
    print(w)
    return licz

print(zad(11,31,4))