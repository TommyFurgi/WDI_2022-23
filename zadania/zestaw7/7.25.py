class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def ostatni(zb):
    fast=zb
    slow=zb
    while 1:
        fast=fast.next.next
        slow=slow.next
        if slow==fast:
            break
    
    fast=zb
    prev=Node(None,zb)
    while fast!=slow:
        fast=fast.next
        prev=prev.next
        slow=slow.next   
    return prev


def pokaz(zb):
    r=zb
    while r is not None:
        print(r.val, end=",")
        r=r.next
    print()

f=Node(9)   
e=Node(7,f)
d=Node(5,e)
c=Node(14,d)
b=Node(5,c)
a=Node(2,b)
zb=Node(3,a)

f.next=b

#pokaz(zb)
print("========")
p=ostatni(zb)
print(p.val)

