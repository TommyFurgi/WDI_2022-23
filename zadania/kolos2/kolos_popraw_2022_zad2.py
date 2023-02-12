'''Zadanie 2 (5 pkt)
Odcinek leżący na osi liczbowej jest opisywany parą liczb całkowitych (a, b). Dana jest tablica
opisująca zbiór takich odcinków. Proszę napisać funkcję zwracającą wartość True, jeżeli z tablicy
można wybrać zbiór odcinków, z których dwa nie zachodzą na siebie, a łączna ich długość wynosi
2022 lub False w przeciwnym wypadku.
'''
def czy_nachodzi(a,b,tab):
    for x,y in tab:
        if x<a<y or x<b<y:
            return True
    return False

def suma(tab):
    suma=0
    for x,y in tab:
        suma+=abs(x-y)
    return suma

def rek(T,pos=0,w=[]):
    if pos==len(T):
        if suma(w)==2022:
            print(w)
            return True
        return False
    (a,b)=T[pos]
    if not czy_nachodzi(a,b,w):
        return rek(T,pos+1,w) or rek(T,pos+1,w+[T[pos]])
    else:
        return rek(T,pos+1,w)

T=[(1,1001),(5,1500),(1002,2024)]
print(rek(T))