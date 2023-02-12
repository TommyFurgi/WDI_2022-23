class Node:
    def __init__(self):
        self.val=None
        self.next=None


def memeber(el,zb): # sprawdzamy czy el nalezy do zbiioru
    r = zb #roboczy wskaznik
    while r.val is not None and r.val<=el:
        if r.val==el:
            return True
        r=r.next

    return False

def insert(el,zb):
    r=zb
    prev=None
    while r.val is not None and r.val<el:
        prev=r
        r=r.next
    if r.val is not None and r.val==el:
        return zb

    new=Node()
    new.val=el
    new.next=r
    if prev.val is None:
        return new
    prev.next=new
    return zb
    
def pop(el,zb):
    r=zb
    prev=None
    while r.val is not None and el>r.val:
        prev=r
        r=r.next

    if r is None or el!=r.val:
        return zb
    
    if el==r.val:
        r=r.next
        if prev is not None:
            prev.next=r
            return zb
        else:
            return r

def pokaz(zb):
    r=zb
    w=[]
    while r is not None:
        w.append(r.val)
        r=r.next
    print(w)

zb=Node()
zb=insert(3,zb)
zb=insert(5,zb)
zb=insert(2,zb)
zb=insert(4,zb)
pokaz(zb)     
print(memeber(3,zb))
zb=pop(3,zb)
pokaz(zb)