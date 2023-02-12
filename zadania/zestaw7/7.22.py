class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


def fun(zb):
    if zb is None:
        return True
    if zb.next==zb:
        return False    
    fast=zb
    slow=zb
    while fast.next != None and fast.next.next != None:
        fast=fast.next.next
        slow=slow.next
        if fast == slow:
            return True

    return False

d=Node(5)
c=Node(14,d)
b=Node(5,c)
a=Node(2,b)
zb=Node(3,a)
d.next=b
print(fun(zb))