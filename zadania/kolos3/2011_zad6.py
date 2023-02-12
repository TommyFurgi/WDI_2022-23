'''
Dany jest łańcuch zawierający liczby naturalne, zbudowany w oparciu o elementy
typu:
pnode = ^node;
node = record
klucz : integer;
next : pnode;
end;
Proszę napisać procedurę, która rozdziela elementy łańcucha wejściowego do 2
łańcuchów, zależnie od reszty dzielenia pola klucz przez 3. Dla reszty równej 1 lub 2,
element należy umieścić odpowiednio w łańcuchu pierwszym lub drugim. Pozostałe
elementy łańcucha wejściowego należy usunąć z pamięci. Do procedury należy przekazać
wskazanie na łańcuch wejściowy, oraz wskazania na powstałe łańcuchy.
'''
from Node import pokaz,stworz
class Node():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def zad(a):
    g1=Node(None,a)#jedynki
    g2=Node(None,None)#dwojki

    p1=g1
    p2=g2
    w=a
    while w is not None:
        if w.val%3==0:
            tmp=w.next
            p1.next=tmp
            w.next=None
            w=tmp
        elif w.val%3==2:
            tmp=w.next
            p1.next=tmp
            p2.next=w
            p2=w
            w.next=None
            w=tmp
        else:
            w=w.next
            p1=p1.next
    
    p=g1.next
    del g1
    r=g2.next
    g2.next=None
    return p,r

a=stworz([2,4,6,8,10,11])
a,b=zad(a)
pokaz(a)
pokaz(b)