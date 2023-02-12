'''. Dane są deklarację reprezentujące listę z klockami mag-mina (patrz zadanie 2).
struct klocek {
int a;
int b;
klocek *next;
};
Lista zawiera zestaw klocków, które można ułożyć w ciąg. Niestety klocki pomieszały się. Proszę napisać funkcję,
która ustawia klocki na liście w ciąg. Uwaga: orientacja klocków w liście jest właściwa.
Na przykład listę: [2|9] [3|6] [8|2] [2|3] [6|2]
należy przekształcić na listę: [8|2] [2|3] [3|6] [6|2] [2|9]
'''
class Node():
    def __init__(self,val1,val2,next=None):
        self.a=val1
        self.b=val2
        self.next=next

def pokaz(zb):
    while zb is not None:
        print("[",zb.a,zb.b,"],",end=" ")
        zb=zb.next
    print()

def zad(zb):  # cos nie dziala
    if zb is None or zb.next is None:
        return zb

    r=zb.next
    first=zb
    last=zb
    zb.next=None
    g=Node(None,None,r)
    prev=g
    while r is not None:
        if first.a==r.b:
            tmp=r.next
            r.next=first
            first=r
            prev.next=tmp

            r=g.next
            prev=g

        elif last.b==r.a:
            last.next=r
            last=r
            tmp=r.next
            r.next=None
            prev=tmp

            r=g.next
            prev=g
        
        else:
            r=r.next
            prev=prev.next
        
    last.next=None
    return first



e=Node(6,2)
d=Node(2,3,e)
c=Node(8,2,d)
b=Node(3,6,c)
a=Node(2,9,b)
pokaz(a)
a=zad(a)
pokaz(a)