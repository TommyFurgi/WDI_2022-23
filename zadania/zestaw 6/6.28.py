def ile_jedynek(tab):
    licznik=0
    for i in tab:
        while i>0:
            if i%2==1:
                licznik+=1
            i//=2
    return licznik

def rek(T,pos=0,w1=[],w2=[],w3=[]):
    if pos==len(T):
        l1=ile_jedynek(w1)
        l2=ile_jedynek(w2)
        l3=ile_jedynek(w3)
        if l1==l2 and l1==l3:
            print(w1,w2,w3)
            return True
        return False

    return rek(T,pos+1,w1+[T[pos]],w2,w3) or rek(T,pos+1,w1,w2+[T[pos]],w3) or rek(T,pos+1,w1,w2,w3+[T[pos]])

T=[2,3,5,7,15]
print(rek(T))

        