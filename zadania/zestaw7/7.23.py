class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


def fun(zb):
    if zb is None:
        return 0
    if zb.next==zb:
        return 1    
    fast=zb.next
    slow=zb
    while fast != slow:
        fast=fast.next.next
        slow=slow.next

    counter=1
    slow=slow.next
    while fast!=slow:
        counter+=1
        slow=slow.next

    return counter

d=Node(5)
c=Node(14,d)
b=Node(5,c)
a=Node(2,b)
zb=Node(3,a)
d.next=b
print(fun(zb))