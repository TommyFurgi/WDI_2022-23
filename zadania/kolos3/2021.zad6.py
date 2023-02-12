'''Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
class Node
..def init(self,val):
....self.val = val
....self.next = None
Zbiór mnogościowy liczb naturalnych reprezentowany jest przez listę o uporządkowanych rosnąco ele-
mentach. Proszę napisać funkcję iloczyn(z1,z2,z3), która przekształca 3 listy (zbiory) z1,z2,z3 w jedną
listę (zbiór) zawierającą elementy będące częścią wspólna zbiorów z1,z2,z3. Funkcja powinna zwrócić
wskazanie do listy wynikowej'''

from Node import stworz,pokaz
class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
    
def iloczyn2(a,b):
    w=Node(0)
    r=w
    while a is not None and  b is not None:
        if a.val==b.val:
            r.next=Node(a.val)
            r=r.next
            a=a.next
            b=b.next
        elif a.val>b.val:
            b=b.next
        else:
            a=a.next

    r.next=None
    tmp=w.next
    w.next=None
    return tmp

def iloczyn(z1,z2,z3):
    return (iloczyn2(iloczyn2(z1,z2),z3))

a=stworz([2,3,4,5,6,7,8,9,10,11,12])
b=stworz([2,4,6,8,10,12])
c=stworz([3,6,9,12])
zb=iloczyn(a,b,c)
pokaz(zb)
'''
def iloczyn(z1,z2):
    g1=Node(None)
    g1.next=None
    prev=g1
    while z1 is not None and z2 is not None:
        if z1.val==z2.val:
            prev.next=z1
            z1=z1.next
            z2=z2.next
            prev=prev.next
        elif z1.val>z2.val:
            z2=z2.next
        else:
            z1=z1.next
    prev.next=None
    tmp=g1.next
    g1.next=None
    return tmp


'''