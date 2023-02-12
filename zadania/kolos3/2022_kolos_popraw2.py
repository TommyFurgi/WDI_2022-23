# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# Zbiór mnogościowy liczb naturalnych reprezentowanych jest przez listę o uporządkowanych rosnąco
# elementach. Proszę napisać funkcję iloczyn(z1, z2, z3), która przekształca 3 listy (zbiory) z1, z2,
# z3 w jedną listę (zbiór) zawierającą elementy będące częścią wspólną zbiorów z1, z2, z3. Funkcja
# powinna zwrócić wskazanie do listy wynikowej
from Node import pokaz,stworz

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = None

def zad(a,b,c):
    return iloczyn(a,iloczyn(b,c))

def iloczyn(a,b):
    w=Node(None,None)
    r=w
    while a is not None and b is not None:
        if a.val==b.val:
            r.next=a
            r=r.next
            a=a.next
            b=b.next
        elif a.val>b.val:
            b=b.next
        else:
            a=a.next
    r.next=None
    r=w.next
    w.next=None
    return r




a = stworz([1, 2, 3, 5, 7, 8])
b = stworz([2, 4, 5, 7, 8])
c = stworz([0, 2, 5, 8, 12, 24])

i=zad(a,b,c)
pokaz(i)