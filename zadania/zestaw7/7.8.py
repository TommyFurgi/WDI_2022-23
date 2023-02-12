class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def usun_co_drugi(zb): #nie dziala
    curr = zb
    while curr.next is not None:
        tmp = curr.next
        tmp=tmp.next
        curr.next = tmp

        curr = curr.next

        return zb
    

def insert(el,zb):
    r=zb
    prev=None
    while r.val is not None and r.val<el:
        prev=r
        r=r.next
    if r.val is not None and r.val==el:
        return zb

    new=Node(el)
    new.next=r
    if prev is None:
        return new
    prev.next=new
    return zb

def pokaz(p):
    while p is not None:
        print(p.val)
        p=p.next


zb=Node(24)
zb=insert(2,zb)
zb=insert(7,zb)
zb=insert(5,zb)
zb=insert(12,zb)
zb=insert(3,zb)
pokaz(zb)
print("=========")
zb=usun_co_drugi(zb)
pokaz(zb)