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

def revers(zb):
    if zb.next is None:
        return zb
    
    prev=revers(zb.next)
    q=prev
    while q.next != None:
        q=q.next
    q.next=zb
    zb.next=None
    return prev

p=Node(None)
insert(2,p)
insert(7,p)
insert(5,p)
pokaz(p.next)
p.next=revers(p.next)
pokaz(p.next)