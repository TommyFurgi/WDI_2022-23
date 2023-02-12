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
    r=zb.next
    while r is not None:
        print(r.val)
        r=r.next


zb=Node(0)
zb=insert(2,zb)
zb=insert(7,zb)
zb=insert(5,zb)
pokaz(zb)