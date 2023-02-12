from Node import stworz,pokaz
class Node():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


def zad(a):
    g1=Node(None)
    g2=Node(None)
    g3=Node(None)

    w1=g1
    w2=g2
    w3=g3

    while a is not None:
        if a.val<8:
            w1.next=a
            w1=w1.next
        elif a.val>24:
            w3.next=a
            w3=w3.next
        else:
            w2.next=a
            w2=w2.next
        a=a.next
    
    w1.next=g2.next
    w2.next=g3.next
    w3.next=None

    tmp=g1.next
    g1.next=None
    g2.next=None
    g3.next=None
    return tmp


a=stworz([2,5,17,1,233,12,44,12,3])
zb=zad(a)
pokaz(zb)