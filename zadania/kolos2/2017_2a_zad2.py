'''Zadanie 2.
Dana jest tablica int t[9], w której nale»y umie±ci¢ liczby od 1 do 9 tak, aby byªy speªnione warunki:
1) warto±ci na s¡siednich polach tablicy musz¡ si¦ ró»ni¢ o co najmniej 2
2) liczby pierwsze nie mog¡ zajmowa¢ s¡siednich pól tablicy
Warto±¢ 1 zostaªa ju» umieszczona w pierwszym (pod indeksem 0) elemencie tablicy. Prosz¦ napisa¢ program,
który wypisuje wszystkie poprawne rozmieszczenia liczb w tablicy.
'''
import math
def czy_pierwsza(liczba): 
    if liczba == 2 or liczba == 3:
        return True
    if liczba %2 == 0 or liczba%3==0 or liczba<=1:
        return False
    i=5
    while int(math.sqrt(liczba))+1>i:
        if liczba%i == 0:
            return False
        i+=2
        if liczba%i == 0:
            return False
        i+=4
    return True

def czy_nalezy(t,n):
    for i in t:
        if i==n:
            return True
    return False

def rek(t=[1,0,0,0,0,0,0,0,0],pos=1):
    if pos==len(t):
        print(t)
        return True
        
    for i in range(1,10):
        if t[pos-1]+1!=i and i+1!=t[pos-1]:
            if not czy_pierwsza(t[pos-1]) or not czy_pierwsza(i):
                if not czy_nalezy(t,i):
                    t[pos]=i
                    if rek(t,pos+1):
                        return True

    t[pos-1]=0
    return False

rek()