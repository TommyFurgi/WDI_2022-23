class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def usun(zb):
    if zb is None or zb.next is None:
        return
    flag=False
    r=zb
    p=r.next
    while p is not None:
        if p.val%r.val!=0:
            if flag==False:
                flag=True
            else:
                zb.next=r
                zb=zb.next
        r=r.next
        p=p.next
    zb.next=None

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
usun(zb)
print("=======")
pokaz(zb)