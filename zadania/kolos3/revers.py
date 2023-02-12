from Node import pokaz,stworz
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

a=stworz([2,3,4,5,6])

def revers(a):
    if a.next==None:
        return a

    prev=revers(a.next)
    q=prev
    while q.next is not None:
        q=q.next

    a.next=None
    q.next=a
    return prev

a=revers(a)
pokaz(a)