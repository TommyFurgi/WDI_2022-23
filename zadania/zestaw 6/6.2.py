def waga(liczba):
    licznik=0
    i=2
    while liczba!=1:
        if liczba%i==0:
            licznik+=1
            while liczba%i==0:
                liczba//=i
        i+=1
    return licznik

def rek(T,i=0,n1=0,n2=0,n3=0):
    if i==len(T):
        return True
    
    if waga(T[i])==n1 or n1==0:
        n1=waga(T[i])
    elif waga(T[i])==n2 or n2==0:
        n2=waga(T[i])
    elif waga(T[i])==n3 or n3==0:
        n3=waga(T[i])
    else:
        return False

    return rek(T,i+1,n1,n2,n3)

T=[2,6,30,64,4]
print(rek(T))