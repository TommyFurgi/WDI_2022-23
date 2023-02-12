class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def insert(el,zb):
    r=zb.next
    prev=zb
    while r is not None and r.val<el:
        prev=r
        r=r.next
    if r is not None and r.val==el:
        return zb

    new=Node(el)
    new.next=r
    if prev is None:
        return new
    prev.next=new
    return zb

def pokaz(zb):
    r=zb
    while r is not None:
        print(r.val)
        r=r.next

def iteracyjnie(zb1,zb2):
    r=Node(None)
    zb=r
    while zb1 is not None or zb2 is not None:
        if zb1 is None:
            r.next=zb2
            return zb.next
        if zb2 is None:
            r.next=zb1
            return zb.next
        
        if zb1.val==zb2.val:
            r.next=zb1
            zb1=zb1.next
            zb2=zb2.next
        elif zb1.val>zb2.val:
            r.next=zb2
            zb2=zb2.next
        else:
            r.next=zb1
            zb1=zb1.next
        r=r.next
    return zb.next

def rek(zb1,zb2):
    if zb1 is None:
        return zb1
    if zb2 is None:
        return zb2
    
    if zb1.val < zb2.val:
        zb1.next=rek(zb1.next,zb2)
        return zb1
    if zb2.val == zb1.val:
        zb1.next=rek(zb1.next,zb2.next)
        return zb1
    zb2.next=rek(zb1,zb2.next)
    return zb2

p=Node(None)
insert(2,p)
insert(7,p)
insert(5,p)

q=Node(None)
insert(3,q)
insert(9,q)
insert(1,q)

m=Node(None)
m.next=iteracyjnie(p.next,q.next)
pokaz(m.next)