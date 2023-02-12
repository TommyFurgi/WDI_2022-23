class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def usun_el(zb,el):
    if zb is None:
        new=Node(el,None)
        return new
    
    if zb.val==el:
        return zb.next

    r=zb
    prev=None
    while r is not None:
        if r.val==el:
            prev.next=r.next
            r.next=None
            return zb

        prev=r
        r=r.next

    new=Node(el,None)
    prev.next=new
    return zb

def pokaz(r):
    while r is not None:
        print(r.val, end=",")
        r=r.next
    print()

d=Node(8,None)
c=Node(5,d)
b=Node(3,c)
a=Node(14,b)

pokaz(a)
a=usun_el(a,4)
pokaz(a)