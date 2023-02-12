class Node:
    def __init__(self,val,prev=None,next=None):
        self.val=val
        self.prev=prev
        self.next=next

def pokaz(zb):
    r=zb
    while r is not None:
        print(r.val, end=",")
        r=r.next
    print()

def jedynki(n):
    s=0
    while n>0:
        s+=n%2
        n//=2
    return s

def usun(zb):
    wartownik=Node(0,None,zb)
    zb.prev=wartownik
    curr=zb
    p=wartownik
    n=zb.next
    while curr is not None:
        if jedynki(curr.val)%2==1:
            tmp=curr.next
            curr.next=None
            curr.prev=None
            p.next=n
            if n is not None:
                n.prev=p
            curr=tmp
        else:
            curr=curr.next
            p=p.next
        if n is not None:
            n=n.next

    tmp=wartownik.next
    if tmp is not None:
        tmp.prev=None
    wartownik.next=None
    return tmp


d=Node(5)
c=Node(14,None,d)
b=Node(1,None,c)
a=Node(3,None,b)
zb=Node(2,None,a)
c.prev=b
b.prev=a
a.prev=zb
d.prev=c

pokaz(zb)
zb=usun(zb)
print(jedynki(14))
print(jedynki(2))
print("=======")
pokaz(zb)#3,5
