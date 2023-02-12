'''Proszę napisać funkcję two(p), która otrzymuje wskazanie na listę i rozdziela elementy listy do dwóch
list. W pierwszej powinny znaleźć się elementy, które w liście wejściowej występowały dokładnie dwa
razy, a w drugiej wszystkie pozostałe. Funkcja powinna zwrócić wskaźniki do powstałych dwóch list.
'''
class Node():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def podziel(zb):
    guard=Node(None)
    guard.next=zb
    licz=0
    a=zb
    druga=Node(None)
    l=druga
    while a is not None:
        licz=0
        q=guard.next
        while q is not None:
            if q.val==a.val:
                licz+=1
            q=q.next
        if licz==2:
            value=a.val
            while a is not None and a.val==value:
                a=a.next
            prev=guard
            t=guard.next
            while t is not None:
                if t.val==value:
                    tmp=t.next
                    l.next=t
                    l=l.next
                    t.next=None
                    prev.next=tmp
                    t=tmp
                else:
                    prev=prev.next
                    t=t.next
        else:
            a=a.next

    return guard.next,druga.next

def pokaz(zb):
    r=zb
    while r is not None:
        print(r.val, end=",")
        r=r.next
    print()


d=Node(5)
c=Node(5,d)
b=Node(6,c)
a=Node(1,b)
zb=Node(1,a)

pokaz(zb)
a,b=podziel(zb)
pokaz(a)
pokaz(b)