'''
Napisz funkcję, która przyjmuje wskaźnik do początku jednokierunkowego
łańcucha odsyłaczowego, a następnie przenosi na początek wszystkie elemen-
ty, w których zapisie ósemkowym występuje nieparzysta liczba piątek.
'''
from Node import pokaz,stworz
class Node():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def ile_5(l):
    ile=0
    while l>0:
        if l%8==5:
            ile+=1
        l//=8
    return ile

def zad(a):
    w=Node(None,a)
    prev=w
    r=a
    while r is not None:
        if ile_5(r.val)%2==1:
            prev.next=r.next
            tmp=r.next
            r.next=w.next
            w.next=r
            r=tmp
        else:
            prev=prev.next
            r=r.next
    return w.next

a=stworz([2,3,5,15,45,22,21])
a=zad(a)
pokaz(a)