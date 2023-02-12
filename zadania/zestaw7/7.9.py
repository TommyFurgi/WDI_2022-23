class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


def zwieksz_o_1(r): # z wartownikiem
    if r.next is None:
        new=Node(1,None)
        r.next=new
        return 
    r=r.next

    while r.next is not None:
        prev=r
        r=r.next

    if r.val<9:
        r.val=r.val+1
    else:
        prev.val=prev.val+1
        r.val=0
    return 

def pokaz(r):
    r=r.next
    while r is not None:
        print(r.val, end="")
        r=r.next
    print()

d=Node(8,None)
c=Node(5,d)
b=Node(3,c)
a=Node(0,b)

pokaz(a)
zwieksz_o_1(a)
pokaz(a)