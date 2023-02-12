class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def warunek(liczba):
    ile=0
    while liczba>0:
        if liczba%8==5:
            ile+=1
        liczba//=8
    if ile%2==0:
        return True
    return False
    

def przenies(zb):
    if zb is None:
        return zb
    prev=zb
    r=zb.next
    while r is not None:
        if warunek(r.val):
            prev.next=r.next
            tmp=r.next
            r.next=zb
            zb=r
            r=tmp
        else:
            prev=prev.next
            r=r.next
    return zb


def pokaz(zb):
    r=zb
    while r is not None:
        print(r.val, end=",")
        r=r.next
    print()

d=Node(5)
c=Node(14,d)
b=Node(1,c)
a=Node(2,b)
zb=Node(2,a)

pokaz(zb)
zb=przenies(zb)
print("=======")
pokaz(zb)
print(warunek(14))