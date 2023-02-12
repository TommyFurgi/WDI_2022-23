'''Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
class Node:
..def init (self,val,next=None):
....self.val = val
....self.next = next
Lista zawiera wartości będące liczbami naturalnymi Proszę napisać funkcję repair(p), (p wskazuje
na pierwszy element listy) która przekształca listę tak aby liczby parzyste znalazły się na końcu listy.
Funkcja powinna zwrócić wskazanie na przekształconą listę.
Komentarz: Można założyć, że lista wejściowa liczy więcej niż 2 elementy.
'''
from Node import pokaz,stworz
class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def repair(p):
    lista2=Node(None)
    k=lista2
    g=Node(None)
    g.next=p
    prev=g
    r=p
    while p is not None:
        if p.val%2==0:
            prev.next=p.next
            k.next=p
            k=k.next
            tmp=p.next
            p.next=None
            p=tmp

        else:
            p=p.next
            prev=prev.next

    prev.next=lista2.next
    lista2.next=None
    tmp=g.next
    g.next=None
    return tmp


a=stworz([2,5,6,78,9,4,3,5,2,44])
pokaz(a)
a=repair(a)
pokaz(a)
