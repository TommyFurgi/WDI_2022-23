class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


def usun(zb):
    guard=Node(0,zb)
    r=zb
    usuwany=None
    ile=0
    prev=guard
    while r is not None:
        if r.next is not None and r.val == r.next.val:
            usuwany=r.val
            while r is not None and r.val==usuwany:
                tmp=r.next
                r.next=None
                r=tmp
                ile+=1
                
            prev.next=r
        else:
            prev=prev.next
            r=r.next
    zb=guard.next
    guard.next=None
    return ile

def pokaz(zb):
    r=zb
    while r is not None:
        print(r.val, end=",")
        r=r.next
    print()


d=Node(16)
c=Node(5,d)
b=Node(5,c)
a=Node(3,b)
zb=Node(2,a)

pokaz(zb)
print("========")
print(usun(zb))
