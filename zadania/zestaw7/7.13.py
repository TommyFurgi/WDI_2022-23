class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


def fun(zb):
    if zb.next == None:
        return 
    r=zb
    p=zb.next
    while p is not None:
        if p.val > r.val:
            zb.next=p
            zb=zb.next
        p=p.next
        r=r.next
    zb.next=None


def pokaz(zb):
    r=zb
    while r is not None:
        print(r.val)
        r=r.next
d=Node(5)
c=Node(14,d)
b=Node(1,c)
a=Node(2,b)
zb=Node(15,a)

pokaz(zb)
fun(zb)
print("=======")
pokaz(zb)
