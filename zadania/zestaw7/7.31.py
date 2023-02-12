class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def fun(Dhead,Whead1,Whead2):
    counter=0
    p1=Whead1
    p2=Whead2
    r=Dhead.next
    while r is not None:
        if r.val>0 and r.val%2==0:
            p1.next=r
            p1=p1.next
            r=r.next
        elif r.val<0 and r.val%2==1:
            p2.next=r
            p2=p2.next
            r=r.next
        else:
            counter+=1
            temp=r
            r=r.next
            temp.next=None
    p2.next=None
    p1.next=None
    return counter